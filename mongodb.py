import pymongo

class mongodbconnection:
    def __init__(self,username,password,db_name,db_collection_name):
        self.username = username
        self.password = password
        self.url = f"mongodb+srv://{username}:{password}@cluster0.vjj8k4u.mongodb.net/?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(self.url)
        self.db = self.client[db_name]
        self.coll1 = self.db[db_collection_name]
       
    def insert(self,dic):
        inserts = self.coll1.insert_one(dic)
        return inserts