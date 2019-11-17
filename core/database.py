from pymongo import MongoClient
from CONFIG import CONNECTION, CLUSTER, DB


class DbClient:
    """CREATES A CONNECTION TO YOUR DATABASE"""
    def __init__(self):
        cluster = MongoClient(CONNECTION)
        db = cluster[CLUSTER]
        self.collection = db[DB]

    def __call__(self, *args, **kwargs):
        return self.collection


class Database(DbClient):
    def init_db(self):
        try:
            self.collection.insert_one(self.db_layout())
            return
        except:
            return

    def delete_db(self):
        try:
            self.collection.delete_one({"_id": 00})
            return
        except:
            return


    def db_layout(self):
        default_data = {
            "_id": 00,
            "humidity": [],
            "temp": []
        }

        return default_data