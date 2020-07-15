#!flask/bin/python
import pymongo
from flask import Flask, jsonify, abort
from healthcheck import HealthCheck

def init_api():

    app = Flask(__name__)
    app.logger.info("Loading settings from settings.py")
    app.config.from_pyfile('settings.py')
    app.logger.info("mongo uri configured for api %s",
                    app.config.get("MONGO_URI"))

    mongoclient = pymongo.MongoClient(app.config.get("MONGO_URI"))
    health = HealthCheck()

    def check_mongo_available():
        
        try:
            mongoclient = pymongo.MongoClient(app.config.get("MONGO_URI"), serverSelectionTimeoutMS = 2000)
            mongoclient.server_info() # will throw an exception
        except:
            app.logger.info("Error establishing connection to mongodb:%s", app.config.get("MONGO_URI"))
            return False, "mongodb failed connection"
        return True, "mongodb ok"

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
        if(movie is None):
            return abort(404, 'movie could not be found')

        movie['_id'] = str(movie['_id'])
        return jsonify(movie)

    health.add_check(check_mongo_available)
    app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda:
                    health.run())
    return app
