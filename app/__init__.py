from flask import Flask


def create_app():
    app = Flask(__name__.split(".")[0])
    register_blueprints(app)
    return app


def register_blueprints(app):

    from app.client.endpoints import client
    app.register_blueprint(client)
