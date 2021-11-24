import asyncio
import logging
import os
from typing import Optional, List

import numpy as np
import pandas as pd
from binance import AsyncClient, Client
from dotenv import load_dotenv

from agents import Agent
from analyser.algo.order_algo import OrderAlgo, OrderExecutor
from analyser.algo.simple_order_algo import SimpleOrderAlgo
from data.account import Balance, SymbolInfo, AccountOrder, Order
from data.tick import MiniTicker
from db_manager import DBManager

log = logging.getLogger(Agent.OrderAgent)

load_dotenv()


class OrderAgent(OrderExecutor):
    client: AsyncClient
    db_manager: DBManager
    info: SymbolInfo
    base_asset: Balance
    quote_asset: Balance
    orders: List[Order]
    update_window_with_order: float
    update_window_without_order: float

    def __init__(self, symbol, *args, **kwargs):
        self.api_key = os.environ.get("API_KEY")
        self.secret_key = os.environ.get("SECRET_KEY")
        self.selected_pair = symbol  # "NBSUSDT"
        self.db_manager = DBManager()
        self.order_point = None
        self.profit_margin = 0.75
        self.agency_fee = 0.02
        self.base_asset_in_hand = 11
        self.update_window_without_order = 15
        self.update_window_with_order = 1
        self.order_algo: OrderAlgo = SimpleOrderAlgo(
            symbol=self.selected_pair,
            order_executor=self,
            options={
                "p_ab": 0.3,
                "p_bc": 0.5,
                "p_de": 0.5,
                "p_ef": 0.1,
            }
        )

    async def start(self):
        await self.db_manager.init()
        self.client = await AsyncClient.create(self.api_key, self.secret_key)
        await self.update()

    async def update(self):
        orders = await self.client.get_open_orders(symbol=self.selected_pair)
        log.info(f"{len(orders)} open orders")
        self.orders = [AccountOrder(**o) for o in orders]

        orders_cursor = self.db_manager.orders.find({'is_open': True, 'symbol': self.selected_pair})
        orders = await orders_cursor.to_list(length=100)
        orders = [Order(**o) for o in orders]
        log.info(f"{len(orders)} open orders in db")
        log.info(f"{orders}")
        await self.order_algo.update_orders(orders)

        info: Optional[dict] = await self.client.get_symbol_info(self.selected_pair)
        self.info: SymbolInfo = SymbolInfo(**info)

        balance = await self.client.get_asset_balance(asset=self.info.baseAsset)
        self.base_asset: Balance = Balance(**balance)

        balance = await self.client.get_asset_balance(asset=self.info.quoteAsset)
        self.quote_asset: Balance = Balance(**balance)

        log.info(f"{self.quote_asset=} {self.base_asset=}")

    async def execute(self, *args, **kwargs):
        while True:
            result = await self.client.get_ticker(symbol=self.selected_pair)
            ticker: MiniTicker = MiniTicker.from_json(result)
            await self.db_manager.ticks.insert_one(result)

            history_list = await self.client. \
                get_historical_klines(self.selected_pair, Client.KLINE_INTERVAL_1MINUTE, "1 hour ago UTC")
            history_list = np.array(history_list)
            history_data = pd.DataFrame(data=history_list[:, 1:6][::-1],
                                        columns=["open", "high", "low", "close", "volume"])
            w_data = history_data["close"].astype(np.float).values

            self.orders = await self.order_algo.update(w_data, ticker)

            if len(self.orders) > 0:
                await asyncio.sleep(self.update_window_with_order)
            else:
                await asyncio.sleep(self.update_window_without_order)

    async def on_buy_order(self, ticker: MiniTicker) -> Order:
        log.info("Place Buy Request")
        await self.update()
        decimals = self.check_decimals()
        quantity = self.base_asset_in_hand / ticker.close_price
        quantity += quantity * (100 + self.agency_fee) / 100
        quantity = round(quantity, decimals)
        log.info(f"{ticker.symbol=} {ticker.close_price=} {quantity=}")

        price_to_buy = ticker.close_price * quantity
        if price_to_buy > self.quote_asset.free:
            log.info("Not Enough Money")
            return None

        res = await self.client.order_market_buy(symbol=self.selected_pair, quantity=quantity)
        self.db_manager.placed_orders.insert_one(res)
        await self.update()
        order = Order(
            symbol=self.selected_pair,
            orderId=res['orderId'],
            qty=quantity,
            price=ticker.close_price,
            side="BUY",
            time=self.time_delta,
            is_open=True,
        )
        res = await self.db_manager.orders.insert_one(order.dict_without_id)
        log.info(f"{res=}")
        order._id = res.inserted_id
        return order

    async def on_sell_order(self, order: Order, tick: MiniTicker) -> Order:
        log.info(f"Place Sell Request")
        current_price = tick.close_price
        order_place_price = order.price
        profit = (current_price - order_place_price) * 100 / order_place_price
        log.info(f"{tick.symbol} {profit=}")

        if profit > self.profit_margin:
            quantity = round(order.qty, self.check_decimals())
            res = await self.client.order_market_sell(symbol=order.symbol, quantity=quantity)
            self.db_manager.placed_orders.insert_one(res)
            self.order_point = None
            await self.update()
            print(f"BUY {order_place_price} SELL {current_price} PROFIT {profit}%")
            order.is_open = False
            await self.db_manager.orders.replace_one({'_id': order._id}, {**order.dict_without_id, 'is_open': False})
        return order

    def check_decimals(self):
        val = self.info.filters[2]['stepSize']
        decimal = 0
        is_dec = False
        for c in val:
            if is_dec is True:
                decimal += 1
            if c == '1':
                break
            if c == '.':
                is_dec = True
        return decimal
