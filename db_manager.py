import motor
import motor.motor_asyncio


class DBManager:
    db_client: motor.motor_asyncio.AsyncIOMotorClient
    db: motor.motor_asyncio.AsyncIOMotorDatabase

    async def init(self):
        self.db_client = motor.motor_asyncio.AsyncIOMotorClient('localhost', 27017)
        self.db = self.db_client.crypto_bot

    @property
    def ticks(self):
        return self.db.ticks

    @property
    def snapshots(self):
        return self.db.snapshots

    @property
    def orders(self):
        return self.db.orders

    @property
    def placed_orders(self):
        return self.db.placed_orders

    @property
    def signals(self):
        return self.db.signals
