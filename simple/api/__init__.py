"""

Ресурсы приложения app


"""

from flask_restful import Api
from flask.blueprints import Blueprint

from simple.api.resources.hello import HelloResource
from simple.api.resources.auth import AuthResource

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)

api.add_resource(HelloResource, "/hello")
api.add_resource(AuthResource, "/auth/login")
