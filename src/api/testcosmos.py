import os

from pymongo import MongoClient

db_name = os.getenv("MONGO_DB")
host = os.getenv("MONGO_HOST")
port = 10255
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
args = "ssl=true&retrywrites=false&ssl_cert_reqs=CERT_NONE"

connuri = f"mongodb://{username}:{password}@{host}:{port}/{db_name}/?{args}"
client = MongoClient(connuri)

db = client[db_name]
user_collection = db['user']

# Save to the DB
user_collection.insert_one({"email": "amer@foobar.com"})

# Query the DB
for user in user_collection.find():
    print(user)
