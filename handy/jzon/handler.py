import json

def json2dict(str):
    return json.loads(str)

def dict2json(dict_):
    return json.dumps(dict_)

import os

def load(filename):
    absolutepath = os.path.realpath(filename)    
    if not os.path.exists(absolutepath): return
    with open(absolutepath, 'r') as file:
        return json.loads(file.read())
    return

def save(dict_,filename,ensure_ascii = False):
    with open(os.path.realpath(filename), 'w') as file:
        #string = json.dumps(dict_,ensure_ascii=ensure_ascii, sort_keys=True, indent=4)#.replace(",", ",\n")
        string = json.dumps(dict_, sort_keys=True, indent=4)#.replace(",", ",\n")
        file.write(string)
    