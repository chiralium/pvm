from pymongo import MongoClient
import os

class MongoDB:
    def __init__(self):
        self.__database = os.environ.get('MONGO_DB')

        self.__conn = MongoClient(
            'mongo',
            username=os.environ.get('MONGO_U'),
            password=os.environ.get('MONGO_P'),
            authSource=self.__database,
            authMechanism='SCRAM-SHA-256'
        )

        self.__db = self.__conn[self.__database]

    def __to_dict(self, cursor):
        data = []
        for row in cursor:
            data.append(row)
        return data

    def fetch(self, collection):
        return self.__to_dict(
            self.__db[collection].find(
                {},
                {
                    '_id' : False
                }
            )
        )
