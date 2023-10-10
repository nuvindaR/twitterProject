import pymongo

def get_mongodb_client():
    # Initialize the MongoDB client and connect to your MongoDB instance
    client = pymongo.MongoClient("mongodb+srv://tharusha:tharusha@cluster0.um6vd4h.mongodb.net/?retryWrites=true&w=majority")  # Change the connection URL as needed
    return client
