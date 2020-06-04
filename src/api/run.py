import sys
import os

from movieapi import init_api
from dotenv import load_dotenv
from os import environ

def check_env_vars():
   if(os.environ.get("MONGO_URI") == None):
        print("env var MONGO_URI not set!!")
        sys.exit()
        
try:
    app = init_api()
    load_dotenv()
    check_env_vars()

except Exception:
    print("failed to load init api")
    print("Something bad happened", sys.exc_info())

# remember docker does not bind to 127.0.0.1 for some reason hence host=0.0.0.0
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
