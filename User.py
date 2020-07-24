import datetime
import pymongo
from bson.objectid import ObjectId
import configs

class User:
    def __init__(self):
        try:
            self.db = pymongo.MongoClient(configs.mongoUrl, configs.mongoPort)[configs.dbname]
            self.col = self.db['clock']
        except:
            print(Exception)
    def save(self,data):
        data['createTime'] = datetime.datetime.utcnow()
        self.col.insert_one(data)
        result = data
        return result
    def findAll(self):
        results = self.col.find()
        items = []
        for result in results:
            item = result
            del item['_id']
            items.append(item)
        return items

