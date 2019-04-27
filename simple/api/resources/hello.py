from flask import jsonify
from flask import request
from flask_restful import Resource


class HelloResource(Resource):

    def get(self):
        """
        Метод обрабатывает GET запрос и возвращает запись с
        ключем "hello" и значением "world".


        Пример запросаs::

            curl -XGET http://localhost:5000/api/hello


        Пример ответа::

            {
                "hello": "world"
            }
        """
        response = {
            "hello": "world"
        }
        return jsonify(response)
