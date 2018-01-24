from functools import wraps
from flask import Response
import json


def json_result(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        serialized_result = json.dumps(result)
        res = Response(response=serialized_result, mimetype="application/json")

        return res
    return wrapper
