import os
from flask import render_template, Blueprint, send_file


main = Blueprint('main', __name__, template_folder='templates', static_folder='static/gen', static_url_path='/static')


@main.route('/templates/<path:partial>')
def render_partial(partial=None):
    return render_template(partial + '.html')


@main.route('/favicon.ico')
def send_favicon():
    return send_file('static/favicon.ico')


@main.route('/upload/<path:name>')
def upload(name=None):
    return send_file(os.path.join('upload/'+name))

@main.route('/')
@main.route('/<path:path>')
def index(path=None):
    return render_template('index.html')

