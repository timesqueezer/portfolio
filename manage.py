#!env/bin/python
from flask.ext.script import Manager
from flask.ext.assets import ManageAssets

from portfolio import create_app

manager = Manager(create_app)
manager.add_command("assets", ManageAssets)

if __name__ == "__main__":
    manager.run()
