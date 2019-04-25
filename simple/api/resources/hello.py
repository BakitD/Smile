from flask import jsonify
from flask import request
from flask_restful import Resource


class HelloResource(Resource):

    def get(self):
        response = {
            "hello": "world"
        }
        return jsonify(response)
