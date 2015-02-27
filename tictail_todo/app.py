from flask import Flask
from flask.ext.restful import Api

from tictail_todo.views.api import api_bp
from tictail_todo.views.pages import static_pages


app = Flask(__name__, template_folder='templates')
api = Api(app)

app.config.from_object('tictail_todo.config')

app.register_blueprint(static_pages)
app.register_blueprint(api_bp)