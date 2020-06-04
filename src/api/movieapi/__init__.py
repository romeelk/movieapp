#!flask/bin/python
import pymongo
from flask import Flask, jsonify
from os import environ


def init_api():

    app = Flask(__name__)
    app.logger.info("Loading settings from settings.py")
    app.config.from_pyfile('settings.py')
    app.logger.info("mongo uri configured for api %s",
                    app.config.get("MONGO_URI"))

    monogoclient = pymongo.MongoClient(app.config.get("MONGO_URI"))

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
    return app
