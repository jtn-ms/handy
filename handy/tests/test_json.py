from handy.jzon.handler import json2dict, dict2json

def test_conv():
    test = {'a':1,'b':[1,2,3]}
    assert(test == json2dict(dict2json(test)))