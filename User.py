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

    def save(self, data):
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

    def saveLogs(self, data):
        col = self.db['log']
        data['createTime'] = datetime.datetime.utcnow()
        result = col.insert_one(data)
        return result

    def findLogs(self):
        col = self.db['log']
        results = col.find()
        items = []
        for result in results:
            item = result
            del item['_id']
            id = item['student_id']
            item['student_id'] = '********' + id[8:11]
            items.append(item)
        return items
