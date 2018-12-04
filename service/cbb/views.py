from flask import request, jsonify
from flask.views import MethodView


class CbbView(MethodView):
    @staticmethod
    def get():
        username = request.args.get('username')
        password = request.args.get('password')

        data = {
            'username': username,
            'password': password
        }

        return jsonify(data)
