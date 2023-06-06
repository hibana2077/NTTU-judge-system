import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database
db = client["mydatabase"]

# Select the collection
collection = db["mycollection"]

# Insert a document into the collection
document = {"name": "John", "age": 30}
collection.insert_one(document)