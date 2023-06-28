from pymongo import MongoClient
# from script.constants.app_configuration import parser
from script.constants.app_configuration import mongo_uri, db


class MongoLite:
    def __init__(self):
        self.connection = MongoClient(mongo_uri)
        self.db = self.connection[db]

    def for_insert_one(self, collection, dictionary):
        collection_1 = self.db[collection]
        if collection_1.insert_one(dictionary):
            return True
        else:
            return False

    def for_find_one(self, collection, data):
        collection_1 = self.db[collection]
        if collection_1.find_one(data):
            return True
        else:
            return False

    def for_delete_one(self, collection, data):
        collection_1 = self.db[collection]
        if collection_1.delete_one(data):
            return True
        else:
            return False

    def for_update_one(self, collection, data, set):
        collection_1 = self.db[collection]
        if collection_1.update_one(data, set):
            return True
        else:
            return False


mongo = MongoLite()
