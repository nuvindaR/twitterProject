from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URL")

def db_connection():
    client =MongoClient(MONGODB_URI)

    return client