import pymongo
class MongoConfig:


    def __init__(self):
        self.connect_string = "mongodb+srv://aravindhsiva9:x3TGgsm1TSYD7kzL@cluster0.hg9a4yb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = pymongo.MongoClient(self.connect_string)
        self.db = self.client["Collection_one"]
        self.collection = self.db["bdd"]


    