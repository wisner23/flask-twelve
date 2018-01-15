from flask import Flask
from app.client.endpoints import client

app = Flask("flask-twelve")
app.register_blueprint(client)