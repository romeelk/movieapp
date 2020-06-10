import requests
import json

from flask import Flask, render_template


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

    @app.route('/Movies')
    def movies():
        try:
            app.logger.info(app.config.get("MOVIEAPIURL"))
            response = requests.get(app.config.get("MOVIEAPIURL"))
            movies = json.loads(response.text)
            return render_template('movies.html', movies=movies['movies'])
        except Exception:
            return render_template('unhandled.html'), 500

    @app.route('/')
    def home():
        return render_template('welcome.html')  # render a template
    return app
