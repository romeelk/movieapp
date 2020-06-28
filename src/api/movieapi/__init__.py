#!flask/bin/python
import pymongo
from flask import Flask, jsonify
from bson.json_util import dumps


def init_api():

    app = Flask(__name__)
    app.logger.info("Loading settings from settings.py")
    app.config.from_pyfile('settings.py')
    app.logger.info("mongo uri configured for api %s",
                    app.config.get("MONGO_URI"))

    mongoclient = pymongo.MongoClient(app.config.get("MONGO_URI"))

    @app.route('/movies', methods=['GET'])
    def get_movies():

        mymoviesdb = mongoclient["movies"]
        latestmovies = mymoviesdb["latestmovies"]

        documents = latestmovies.find()
        response = []
        for document in documents:
            document['_id'] = str(document['_id'])
            response.append(document)

        return jsonify({'movies': response})

    @app.route('/movie/<title>', methods=['GET'])
    def get_movie(title):

        mymoviesdb = mongoclient["movies"]

        app.logger.info(title)
        movie = mymoviesdb.latestmovies.find_one({'title': title})
        return dumps(movie)
    return app
