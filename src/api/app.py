#!flask/bin/python
import pymongo
import json
from flask import Flask, jsonify

app = Flask(__name__)

monogoclient = pymongo.MongoClient("mongodb://localhost:27017/")

@app.route('/movies', methods=['GET'])
def get_movies():

    mymoviesdb = monogoclient["movies"]
    latestmovies = mymoviesdb["latestmovies"]

    documents = latestmovies.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
   
    return jsonify({'movies': response})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5001)