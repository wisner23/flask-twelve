from flask import Flask
from app.client.endpoints import client


def create_app():
    app = Flask("flask-twelve")
    app.register_blueprint(client)
    return app

