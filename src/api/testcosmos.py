import os

from pymongo import MongoClient

db_name = os.getenv("MONGO_DB")
host = os.getenv("MONGO_HOST")
port = 10255
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
args = "ssl=true&retrywrites=false&ssl_cert_reqs=CERT_NONE"

#connection_uri = f"mongodb://{username}:{password}@{host}:{port}/{db_name}?{args}"
connection_uri = "mongodb://moviecosmos:6JsPXl9xcLNDoSRkmmRNaXzCnLqqFWLFoZIgVoaFj3OZZiJaKOefQQ2RkpUHqn9CgLNK2WHvDjNRjjtNKQqiRw==@moviecosmos.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@moviecosmos@"
client = MongoClient(connection_uri)

db = client[db_name]
user_collection = db['user']

# Save to the DB
user_collection.insert_one({"email": "amer@foobar.com"})

# Query the DB
for user in user_collection.find():
        print(user)
