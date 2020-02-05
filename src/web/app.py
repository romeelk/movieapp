# import the Flask class from the flask module
import requests
import os
import logging
import json

from flask import Flask, render_template


# create the application object
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('notfound.html')  

@app.route('/Movies')
def movies():
    movieappurl  = os.environ.get("MOVIEAPIURL")
    response = requests.get(movieappurl)
    movies = json.loads(response.text)
    for x in movies['movies']:
        print x['title']
    return render_template('movies.html', movies=movies['movies'])  # render a template

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('welcome.html')  # render a template
    
# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
