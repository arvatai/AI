from pymongo import MongoClient

def get_mongo_client(uri="mongodb://localhost:27017/"):
    try:
        client = MongoClient(uri)
        return client
    except Exception as e:
        print(f"An error occurred while connecting to MongoDB: {e}")
        return None
