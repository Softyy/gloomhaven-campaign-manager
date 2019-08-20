import json
from urllib import parse


def dict_to_inline_href(d: dict):
    return f'data:application/json;charset=utf-8,{parse.quote(json.dumps(d))}'
