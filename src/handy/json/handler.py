import json

def json2dict(str):
    return json.loads(str)

def dict2json(dict_):
    return json.dumps(dict_)

def load(filename):
    with open('file') as file:
        return json.loads(file.read())

def save(dict_,filename,ensure_ascii = False):
    with open(filename, 'w') as file:
        string = json.dumps(dict_,ensure_ascii=ensure_ascii).replace(",", ",\n")
        file.write(string)
    