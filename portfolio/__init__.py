from flask import Flask
import os

from portfolio.bundles import js, css, assets
from portfolio.views import main


def create_app(config=None):
    app = Flask(__name__)

    app.config['DEBUG'] = True
    app.config['LESS_BIN'] = os.path.realpath(os.path.join(os.path.dirname(__file__), '../node_modules/less/bin/lessc'))

    if config:
        app.config.from_object(config)

    app.config['ASSETS_DEBUG'] = app.config['DEBUG']

    assets.init_app(app)
    assets.register('js', js)
    assets.register('css', css)

    app.register_blueprint(main)

    return app
