import json

def json2dict(str):
    return json.loads(str)

def dict2json(dict):
    return json.dumps(dict)

def loadfile(filename):
    with open('file') as file:
        return json.loads(file.read())

