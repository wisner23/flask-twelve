from ..resources.mock_data import clients as cl_resource
from flask import url_for


def test_get_clients(client):
    res = client.get(url_for("client.clients"))

    assert res.mimetype == 'application/json'
    assert res.json == cl_resource



