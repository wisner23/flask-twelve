from functools import wraps
import json


def json_result(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return json.dumps(result)
    return wrapper
