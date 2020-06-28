import requests
import json

from flask import Flask, render_template, request



def init_app():

    app = Flask(__name__)
    app.logger.info("Loading settings from settings.py")
    app.config.from_pyfile('settings.py')
    app.logger.info("app configured for api at uri %s",
                    app.config.get("MOVIEAPIURL"))

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
            print(title)
            getmovieurl = app.config.get("MOVIEAPIURL") + "/movie/" + title
        
            response = requests.get(getmovieurl)
            movie = json.loads(response.text)
            print(response.text)
            return render_template('movie.html', movie=movie)
        except Exception:
            return render_template('unhandled.html'), 500
          
    @app.route('/')
    def home():
        return render_template('welcome.html')  # render a template
    return app
