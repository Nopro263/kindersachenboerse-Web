import json
from json import JSONDecodeError

CONFIG = {}


def load(path: str, mode='json'):
    global CONFIG
    with open(path, "r") as file:
        try:
            CONFIG = json.loads(file.read())
        except JSONDecodeError:
            raise TypeError("File was not json decodeable")
