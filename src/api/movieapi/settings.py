from os import environ

MONGO_DBNAME = environ.get('MONGO_DBNAME')
MONGO_URI = environ.get('MONGO_URI')
FLASK_ENV = environ.get('development')
