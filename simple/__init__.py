import os

from flask_script import Manager
from flask_restful import Api

from simple.api import api_blueprint


commandManager = Manager()


def create_app(app):

    init_settings(app)

    init_extensions(app)

    init_blueprints(app)

    return app


def init_blueprints(app):

    app.register_blueprint(api_blueprint, url_prefix="/api")


def init_extensions(app):
    commandManager.app = app


def init_settings(app):
    os.environ.setdefault("APPDATER_API_CONFIG", "settings.py")
    app.config.from_envvar("APPDATER_API_CONFIG")
