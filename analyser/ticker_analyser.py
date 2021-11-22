import logging

from data.tick import AssetSnapshot, MiniTicker

log = logging.getLogger("AssetAnalyser")


class AssetAnalyser:

    def __init__(self, asset_name, time_limits=[30, 60]):
        self.time_limits = time_limits
        self.asset_name = asset_name
        self.ticker_list = {limit: [] for limit in time_limits}

    async def update(self, ticker: MiniTicker):
        for time_limit in self.time_limits:
            self.ticker_list[time_limit].append(ticker)
            snapshots = await self.snapshot()
            snapshot = snapshots[time_limit]
            if snapshot and snapshot.duration_in_seconds > time_limit:
                self.ticker_list[time_limit].pop(0)

    async def snapshot(self):
        snapshots = {}
        for time_limit in self.time_limits:
            ticker_list = self.ticker_list[time_limit]
            snapshot = None
            if len(ticker_list) > 1:
                close_tick: MiniTicker = ticker_list[-1]
                open_tick: MiniTicker = ticker_list[0]
                high_tick: MiniTicker = max(ticker_list, key=lambda tick: tick.close_price)
                low_tick: MiniTicker = min(ticker_list, key=lambda tick: tick.close_price)
                snapshot_temp = AssetSnapshot(
                    symbol=self.asset_name,
                    time_window=time_limit,
                    open_tick=open_tick,
                    close_tick=close_tick,
                    high_tick=high_tick,
                    low_tick=low_tick,
                )
                snapshot = snapshot_temp if snapshot_temp.duration_in_seconds > time_limit else None

            snapshots[time_limit] = snapshot
        return snapshots

    def __len__(self):
        return len(self.ticker_list)
