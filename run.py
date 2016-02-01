#!env/bin/python
import sys

from portfolio import create_app


class ProductionConfig(object):
    DEBUG = False
    TESTING = False

app = create_app(config=ProductionConfig)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-p':
        print(' * Running in production mode')
        app = create_app(config=ProductionConfig)
    else:
        app = create_app()
    app.run(host='0.0.0.0')
