import os

from movieapp import init_app
from dotenv import load_dotenv

try:
    app = init_app()
    load_dotenv()
except:
    print("failed to load init app")
    sys.exit()

# remember docker does not bind to 127.0.0.1 for some reason hence host=0.0.0.0
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
