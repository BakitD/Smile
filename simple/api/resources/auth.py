from flask import jsonify
from flask import request
from flask_restful import Resource

from simple.core.constants import Constants
from simple.core.token import TokenGenerator


class AuthResource(Resource):

    def post(self):
        """
        Метод обрабатывает POST запрос с пустым телом и возвращает
        строку из 12 псевдослучайных символов ASCII и цифр в
        json-формате.


        Пример запроса::

            curl -XPOST http://localhost:5000/api/auth/login


        Пример ответа::

            {
                "token": "3FkiNfxfxDag"
            }

        """
        response = {
            "token": TokenGenerator.generate(Constants.TOKEN_LENGTH)
        }
        return jsonify(response)