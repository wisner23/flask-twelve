from flask import Blueprint, jsonify
from app.resources.mock_data import clients as clients_data


client = Blueprint(name="client", import_name=__name__, url_prefix="/client")


@client.route("/", methods=["GET"])
def clients():
    return jsonify(results=clients_data)
