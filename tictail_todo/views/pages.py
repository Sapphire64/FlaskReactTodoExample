from flask import render_template, Blueprint


static_pages = Blueprint('static_pages', __name__)


@static_pages.route('/')
def show_index():
    return render_template('index.html')
