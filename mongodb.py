import pymongo

#This class will be used for MongoDB database operations and
class mongodbconnection:
    """
    This class will be used for MongoDB database insert_one operation 
    and it will take username,password,database name and collection name
    and will establish connection to mongodb database
    """
    def __init__(self,username,password,db_name,db_collection_name):
        self.username = username
        self.password = password
        self.url = f"mongodb+srv://{username}:{password}@cluster0.vjj8k4u.mongodb.net/?retryWrites=true&w=majority"
        self.client = pymongo.MongoClient(self.url)
        self.db = self.client[db_name]
        self.coll1 = self.db[db_collection_name]
       
    def insert(self,dic):
        """
        This function takes one argument as a dictionary and
        insert the data into mongoDb database and 
        only for one document at a time
        """
        inserts = self.coll1.insert_one(dic)
        return inserts