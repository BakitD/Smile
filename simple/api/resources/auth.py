from flask import jsonify
from flask import request
from flask_restful import Resource

from simple.core.constants import Constants
from simple.core.token import TokenGenerator


class AuthResource(Resource):

    def post(self):
        response = {
            "token": TokenGenerator.generate(Constants.TOKEN_LENGTH)
        }
        return jsonify(response)