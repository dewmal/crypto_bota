import asyncio
import logging
import os

from binance import AsyncClient, Client
from dotenv import load_dotenv

from analyser.order_handler import OrderHandler
from data.tick import MiniTicker
from db_manager import DBManager
import pandas as pd
import numpy as np
from agents import Agent
from matplotlib import pyplot as plt

log = logging.getLogger(Agent.OrderAgent)

load_dotenv()


class OrderAgent:
    client: AsyncClient
    db_manager: DBManager

    def __init__(self, *args, **kwargs):
        self.api_key = os.environ.get("API_KEY")
        self.secret_key = os.environ.get("SECRET_KEY")
        self.selected_pair = "CHESSUSDT"
        self.db_manager = DBManager()
        self.order_point = None
        self.profit_margin = 0.05

    async def start(self):
        await self.db_manager.init()
        self.client = await AsyncClient.create(self.api_key, self.secret_key)

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
            # log.info(f"{history_data.head()}")

            w_data = history_data["close"].astype(np.float).values

            if self.order_point is None:
                buy_point, b_points = OrderHandler().identify_buy_point(w_data, p_ab=0.1, p_bc=0.2)
                log.info(f"{buy_point=} {b_points=}")
                if buy_point:
                    if self.order_point is None:
                        self.order_point = ticker
                        plt.title("BUY POINT")
                        plt.plot(w_data)
                        plt.scatter(b_points, w_data[b_points])
                        plt.show()
            else:
                sell_point, s_points = OrderHandler().identify_sell_point(w_data, p_de=0.5, p_ef=0.1)

                if sell_point:
                    sell_point = sell_point + 0
                    if self.order_point is not None:
                        current_price = ticker.close_price
                        order_place_price = self.order_point.close_price
                        profit = (current_price - order_place_price) / order_place_price
                        if profit > self.profit_margin:
                            self.order_point = None
                            plt.title("SELL POINT")
                            plt.plot(w_data)
                            plt.scatter(s_points, w_data[s_points])
                            plt.show()
                            print(f"BUY {order_place_price} SELL {current_price} PROFIT {profit}%")

        await asyncio.sleep(60)
