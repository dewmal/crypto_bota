import datetime
from dataclasses import asdict

from pydantic.dataclasses import dataclass

"""
{
    "symbol": "LTCBTC",
    "orderId": 1,
    "orderListId": -1, //Unless OCO, the value will always be -1
    "clientOrderId": "myOrder1",
    "price": "0.1",
    "origQty": "1.0",
    "executedQty": "0.0",
    "cummulativeQuoteQty": "0.0",
    "status": "NEW",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "stopPrice": "0.0",
    "icebergQty": "0.0",
    "time": 1499827319559,
    "updateTime": 1499827319559,
    "isWorking": true,
    "origQuoteOrderQty": "0.000000"
    }
"""


@dataclass()
class AccountOrder:
    symbol: str
    orderId: int
    orderListId: int
    clientOrderId: str
    price: float
    origQty: float
    executedQty: float
    cummulativeQuoteQty: float
    status: str
    timeInForce: str
    type: str
    side: str
    stopPrice: float
    icebergQty: float
    time: int
    updateTime: int
    isWorking: bool
    origQuoteOrderQty: float
    is_open: bool = True
    transactTime: int = 0

    @property
    def dict(self):
        return asdict(self)


@dataclass()
class Order:
    symbol: str
    orderId: str
    qty: float
    price: float
    side: str
    time: datetime.datetime
    is_open: bool = True
    _id: str = None

    @property
    def dict(self):
        d = asdict(self)
        return d

    @property
    def dict_without_id(self):
        d = asdict(self)
        del d['_id']
        return d


"""
{
                "symbol": "ETHBTC",
                "status": "TRADING",
                "baseAsset": "ETH",
                "baseAssetPrecision": 8,
                "quoteAsset": "BTC",
                "quotePrecision": 8,
                "orderTypes": ["LIMIT", "MARKET"],
                "icebergAllowed": false,
                "filters": [
                    {
                        "filterType": "PRICE_FILTER",
                        "minPrice": "0.00000100",
                        "maxPrice": "100000.00000000",
                        "tickSize": "0.00000100"
                    }, {
                        "filterType": "LOT_SIZE",
                        "minQty": "0.00100000",
                        "maxQty": "100000.00000000",
                        "stepSize": "0.00100000"
                    }, {
                        "filterType": "MIN_NOTIONAL",
                        "minNotional": "0.00100000"
                    }
                ]
            }
"""


@dataclass()
class SymbolInfo:
    symbol: str
    status: str
    baseAsset: str
    baseAssetPrecision: int
    quoteAssetPrecision: int
    baseCommissionPrecision: int
    quoteCommissionPrecision: int
    quoteOrderQtyMarketAllowed: bool
    quoteAsset: str
    ocoAllowed: bool
    isSpotTradingAllowed: bool
    isMarginTradingAllowed: bool
    icebergAllowed: bool
    ocoAllowed: bool
    quotePrecision: int
    orderTypes: list
    icebergAllowed: bool
    filters: list
    orderTypes: list
    permissions: list


@dataclass
class Balance:
    asset: str
    free: float
    locked: float
