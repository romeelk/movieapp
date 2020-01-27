import flask
import jsonify
import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

movies = [
    {'id': 0,
     'title': 'Once upon a time',
     'director': 'James Smith'}
     ,
      {'id': 1,
     'title': 'The King',
     'director': 'Samuel Jones'} 
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Movie Catalog</h1><p>This site is a prototype API for fiction movies.</p>"

@app.route('/api/v1/movies', methods=['GET'])
def api_all():
    return jsonify(movies)

app.run(host='0.0.0.0',port='5001')

