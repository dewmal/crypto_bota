import datetime
import json

from dataclasses import asdict
from typing import List, Any

from pydantic.dataclasses import dataclass
from pydantic.json import pydantic_encoder

"""
  {
    "e": "24hrMiniTicker",  // Event type
    "E": 123456789,         // Event time
    "s": "BNBBTC",          // Symbol
    "c": "0.0025",          // Close price
    "o": "0.0010",          // Open price
    "h": "0.0025",          // High price
    "l": "0.0010",          // Low price
    "v": "10000",           // Total traded base asset volume
    "q": "18"               // Total traded quote asset volume
}

{
    "symbol": "BNBBTC",
    "priceChange": "-94.99999800",
    "priceChangePercent": "-95.960",
    "weightedAvgPrice": "0.29628482",
    "prevClosePrice": "0.10002000",
    "lastPrice": "4.00000200",
    "lastQty": "200.00000000",
    "bidPrice": "4.00000000",
    "bidQty": "100.00000000",
    "askPrice": "4.00000200",
    "askQty": "100.00000000",
    "openPrice": "99.00000000",
    "highPrice": "100.00000000",
    "lowPrice": "0.10000000",
    "volume": "8913.30000000",
    "quoteVolume": "15.30000000",
    "openTime": 1499783499040,
    "closeTime": 1499869899040,
    "firstId": 28385,   // First tradeId
    "lastId": 28460,    // Last tradeId
    "count": 76         // Trade count
  }


"""


@dataclass
class MiniTicker:
    symbol: str
    event_type: str
    event_time: int
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    base_volume: float
    quote_volume: float
    raw_message: Any

    @property
    def is_valid(self):
        return self.symbol and self.event_type and self.event_time and self.open_price and self.high_price and self.low_price and self.close_price and self.base_volume and self.quote_volume

    @staticmethod
    def from_json_ws(obj):
        return MiniTicker(
            symbol=obj['s'],
            event_type=obj['e'],
            event_time=obj['E'] / 1000,
            open_price=obj['o'],
            high_price=obj['h'],
            low_price=obj['l'],
            close_price=obj['c'],
            base_volume=obj['v'],
            quote_volume=obj['q']
        )

    @staticmethod
    def from_json(obj):
        ticker = MiniTicker(
            symbol=obj['symbol'],
            event_type="24HrTicker",
            event_time=obj['closeTime'] / 1000,
            open_price=obj['openPrice'],
            high_price=obj['highPrice'],
            low_price=obj['lowPrice'],
            close_price=obj['lastPrice'],
            base_volume=obj['volume'],
            quote_volume=obj['quoteVolume'],
            raw_message=obj
        )
        if ticker.is_valid:
            return ticker
        return None

    @property
    def to_json(self):
        return json.dumps(self, indent=4, default=pydantic_encoder)

    @property
    def event_time_as_datetime(self):
        return datetime.datetime.fromtimestamp(self.event_time)

    @property
    def dict(self):
        return asdict(self)


@dataclass
class AssetSnapshot:
    symbol: str
    time_window: int
    high_tick: MiniTicker
    low_tick: MiniTicker
    open_tick: MiniTicker
    close_tick: MiniTicker

    @property
    def is_ready(self):
        return self.high_tick and self.low_tick and self.open_tick and self.close_tick

    @property
    def slope(self):
        if self.duration_timestamp != 0:
            return self.change / -self.duration_timestamp
        else:
            return 0

    @property
    def direction(self):
        return 'up' if self.slope > 0 else 'down'

    @property
    def duration_timestamp(self):
        return self.close_tick.event_time - self.open_tick.event_time

    @property
    def duration(self):
        start_time = datetime.datetime.fromtimestamp(self.open_tick.event_time)
        end_time = datetime.datetime.fromtimestamp(self.close_tick.event_time)
        return end_time - start_time

    @property
    def duration_in_seconds(self):
        return self.duration.seconds

    @property
    def change(self):
        return self.close_tick.close_price - self.open_tick.close_price

    @property
    def change_percent(self):
        return self.change / self.open_tick.close_price

    @property
    def change_percentage(self):
        return int(self.change_percent * 100 * 1000) / 1000

    @property
    def last_24_hour_change(self):
        return self.close_tick.close_price - self.close_tick.open_price

    @property
    def last_24_hour_percent(self):
        return self.last_24_hour_change / self.open_tick.open_price

    @property
    def last_24_hour_percentage(self):
        return int(self.last_24_hour_percent * 100 * 1000) / 1000

    @property
    def open_time(self):
        return datetime.datetime.fromtimestamp(self.open_tick.event_time)

    @property
    def close_time(self):
        return datetime.datetime.fromtimestamp(self.close_tick.event_time)

    @property
    def open(self):
        return self.open_tick.close_price

    @property
    def close(self):
        return self.close_tick.close_price

    @property
    def high(self):
        return self.high_tick.close_price

    @property
    def low(self):
        return self.low_tick.close_price

    @property
    def to_json(self):
        return json.dumps(self, indent=4, default=pydantic_encoder)

    @property
    def dict(self):
        return asdict(self)

    @property
    def is_up(self):
        return self.change_percentage > 0

    @property
    def is_down(self):
        return self.change_percentage < 0

    @property
    def is_up_24(self):
        return self.last_24_hour_percentage > 0

    @property
    def is_down_24(self):
        return self.last_24_hour_percentage < 0


@dataclass()
class TickWindow:
    symbol: str
    time_window: int
    mini_tick_list: List[MiniTicker]

    @property
    def open_time(self):
        return self.mini_tick_list[0].event_time

    @property
    def close_time(self):
        return self.mini_tick_list[-1].event_time

    @property
    def open(self):
        return self.mini_tick_list[0].close_price

    @property
    def close(self):
        return self.mini_tick_list[-1].close_price

    @property
    def high(self):
        return self.mini_tick_list[0].high_price

    @property
    def low(self):
        return self.mini_tick_list[0].low_price

    def __len__(self):
        return len(self.mini_tick_list)


@dataclass()
class Signal:
    symbol: str
    time_window: int
    signal_type: str
    signal_time: int
    signal_direction: str
