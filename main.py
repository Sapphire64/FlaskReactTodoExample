from pydoc import locate

from flask import Flask, request
from flask.ext.restful import Resource, Api


app = Flask(__name__)
app.config.from_object('config')
api = Api(app)

USER_ID = 'mocked_user_id_for_example'

TODO_STORAGE = locate(app.config.get('STORAGE_ENGINE'))()


class TodoListApi(Resource):
    def get(self, todo_id=None):
        if todo_id is not None:
            return TODO_STORAGE.get_item(USER_ID, todo_id)
        return TODO_STORAGE.get_items(USER_ID)

    def post(self):
        return TODO_STORAGE.create_item(
            USER_ID, request.json.get('data')
        )

    def put(self, todo_id):
        return TODO_STORAGE.update_item(
            USER_ID, todo_id, request.json
        )

    def delete(self, todo_id):
        return TODO_STORAGE.remove_item(USER_ID, todo_id)


api.add_resource(TodoListApi, '/todos/', '/todos/<int:todo_id>')


if __name__ == '__main__':
    app.run(debug=True)
