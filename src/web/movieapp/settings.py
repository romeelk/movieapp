from os import environ

MOVIEAPIURL = environ.get('MOVIEAPIURL')
MONGO_DBNAME = environ.get('MONGO_DBNAME')
MONGO_URI = environ.get('MONGO-URI')
FLASK_ENV = environ.get('development')
