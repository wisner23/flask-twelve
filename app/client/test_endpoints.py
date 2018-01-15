from .endpoints import clients
from ..resources.mock_data import clients as cl_resource
from flask import url_for

import json

def test_get_clients():
    assert clients() == json.dumps(cl_resource)


#test_get_clients()