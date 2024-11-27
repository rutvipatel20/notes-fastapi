from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017/notes"

conn = MongoClient(MONGO_URL)