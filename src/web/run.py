import os
import sys


from movieapp import init_app
from dotenv import load_dotenv


def check_env_vars():
    if(os.environ.get("MOVIEAPIURL") is None):
        print("env var MOVIEAPIURL not set!!")
        sys.exit()


try:
    app = init_app()
    load_dotenv()
    check_env_vars()
except Exception:
    print("failed to load init app")
    print("Something bad happened", sys.exc_info())

# remember docker does not bind to 127.0.0.1 for some reason hence host=0.0.0.0
if __name__ == "__main__":
    app.run(host='0.0.0.0')
