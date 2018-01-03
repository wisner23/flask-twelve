from flask import Flask
from app.client.views import client

app = Flask("flask-twelve")

app.register_blueprint(client)
