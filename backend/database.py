from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")

# Create database
db = client["stallx"]

# Create collection
orders_collection = db["orders"]