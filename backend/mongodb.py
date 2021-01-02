from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.db = MongoClient('mongodb://0.0.0.0:8081')
