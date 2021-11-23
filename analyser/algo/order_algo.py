import asyncio
import logging
from abc import ABC, abstractmethod
from typing import List

from data.account import Order
from data.tick import MiniTicker

log = logging.getLogger("OrderAlgoBase")


class OrderExecutor(ABC):

    @abstractmethod
    async def on_buy_order(self, ticker: MiniTicker) -> Order:
        pass

    @abstractmethod
    async def on_sell_order(self, order: Order, tick: MiniTicker) -> Order:
        pass


class OrderAlgo(ABC):
    orders: List[Order] = []

    def __init__(self, symbol, order_executor: OrderExecutor, number_of_orders=1, options: dict = None):
        self.options = options
        self.symbol = symbol
        self.on_buy = order_executor.on_buy_order
        self.on_sell = order_executor.on_sell_order
        self.number_of_orders = number_of_orders

    def on_hand_profit(self, tick: MiniTicker):
        profit = 0
        for order in self.orders:
            profit += (tick.close_price - order.price) * 100 / order.price
        return profit

    async def update(self, history_data, ticker: MiniTicker) -> List[Order]:
        total_profit = self.on_hand_profit(ticker)
        if total_profit > 0:
            log.info(f"{self.symbol} has {total_profit}% profit")

        if len(self.orders) > 0:
            sell_point, other_points = await self.get_sell_point(history_data, self.options)
            if sell_point:
                await self.sell(ticker)

        buy_point, other_points = await self.get_buy_point(history_data, self.options)
        log.info(f"{buy_point=} , {len(self.orders)=},{self.number_of_orders=}")
        if buy_point and len(self.orders) < self.number_of_orders:
            await self.buy(ticker)

        return self.orders

    async def buy(self, ticker: MiniTicker):
        order = await self.on_buy(ticker)
        if order:
            self.orders.append(order)
            log.info(f"{len(self.orders)=},{self.number_of_orders=}")
        await asyncio.sleep(0.01)

    async def sell(self, ticker: MiniTicker):
        for order in self.orders:
            order = await self.on_sell(order, ticker)
            if not order.is_open:
                self.orders.remove(order)
        await asyncio.sleep(0.01)

    @abstractmethod
    async def get_buy_point(self, price_list, options: dict):
        pass

    @abstractmethod
    async def get_sell_point(self, price_list, options: dict):
        pass
