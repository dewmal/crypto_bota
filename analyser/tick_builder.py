import logging
from typing import List

from data.tick import MiniTicker, TickWindow

log = logging.getLogger(__name__)


class TickBuilder:

    def __init__(self, symbol_name, tick_window_size_in_seconds=30, history_limit=1000):
        self.symbol_name = symbol_name
        self.tick_window_size_in_seconds = tick_window_size_in_seconds
        self.history_limit = history_limit

        self.tick_data_list: List[MiniTicker] = []
        self.history = []
        self.window_start_tick: MiniTicker = None
        self.window_end_tick: MiniTicker = None

    async def add(self, tick_data: MiniTicker):
        self.tick_data_list.append(tick_data)
        if self.window_start_tick is None:
            self.window_start_tick = tick_data
        else:
            self.window_end_tick = tick_data
            if self.duration_in_second >= 120:
                await self.build_tick()

    @property
    def duration_in_second(self):
        if self.window_start_tick is None or self.window_end_tick is None:
            return 0
        return (self.window_end_tick.event_time_as_datetime - self.window_start_tick.event_time_as_datetime).seconds

    async def build_tick(self):
        tick_window = TickWindow(
            symbol=self.symbol_name,
            time_window=30,
            mini_tick_list=[*self.tick_data_list]
        )
        self.history.append(tick_window)
        self.tick_data_list = []
        self.window_start_tick = None

        if len(self.history) > self.history_limit:
            self.history.pop(0)

    def __len__(self):
        return len(self.history)
