import requests
import json

from flask import Flask, render_template, request
from healthcheck import HealthCheck


def init_app():

    app = Flask(__name__)
    app.logger.info("Loading settings from settings.py")
    app.config.from_pyfile('settings.py')
    app.logger.info("app configured for api at uri %s",
                    app.config.get("MOVIEAPIURL"))
    health = HealthCheck()

    def check_api_available():
        getapihealth = app.config.get("MOVIEAPIURL") + "/healthcheck"
        response = requests.get(getapihealth)
        if(response.status_code == 200):
            return True, "movieapi ok"
        else:
            return False, "movieapi returned bad status"

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('notfound.html'), 404

    @app.errorhandler(500)
    def unhandled_exception(error):
        return render_template('unhandled.html'), 500

    @app.route('/movies')
    def get_movies():
        try:
            app.logger.info(app.config.get("MOVIEAPIURL"))
            getmovies = app.config.get("MOVIEAPIURL") + "/movies"
            response = requests.get(getmovies)
            movies = json.loads(response.text)
            return render_template('movies.html', movies=movies['movies'])
        except Exception:
            return render_template('unhandled.html'), 500

    @app.route('/movie')
    def movie():
        try:
            app.logger.info(app.config.get("MOVIEAPIURL"))
            title = request.args.get('title')
            getmovieurl = app.config.get("MOVIEAPIURL") + "/movie/" + title
            response = requests.get(getmovieurl)
            if(response.status_code == 404):
                return render_template('notfound.html'), 404

            movie = json.loads(response.text)
            return render_template('movie.html', movie=movie)
        except Exception:
            return render_template('unhandled.html'), 500

    @app.route('/')
    def home():
        return render_template('welcome.html')  # render a template

    health.add_check(check_api_available)
    app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda:
                     health.run())

    return app
