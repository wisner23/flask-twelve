from flask import Blueprint, jsonify
from app.resources.mock_data import clients as clients_data
from ..common.utils import json_result

client = Blueprint(name="client", import_name=__name__, url_prefix="/client")


@client.route("/", methods=["GET"])
@json_result
def clients():
    return clients_data
