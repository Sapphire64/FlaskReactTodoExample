from flask.ext.restful import Resource, Api
from flask import request, Blueprint

from tictail_todo.storage.engine import STORAGE_ENGINE


api_bp = Blueprint('api', __name__)
api = Api(api_bp)


USER_ID = 'mocked_user_id_for_example'


class TodoListApi(Resource):
    def get(self, todo_id=None):
        if todo_id is not None:
            return STORAGE_ENGINE.get_item(USER_ID, todo_id)
        return STORAGE_ENGINE.get_items(USER_ID)

    def post(self):
        return STORAGE_ENGINE.create_item(
            USER_ID, request.json.get('data')
        )

    def put(self, todo_id):
        return STORAGE_ENGINE.update_item(
            USER_ID, todo_id, request.json
        )

    def delete(self, todo_id):
        return STORAGE_ENGINE.remove_item(USER_ID, todo_id)


api.add_resource(TodoListApi, '/todos/', '/todos/<string:todo_id>')