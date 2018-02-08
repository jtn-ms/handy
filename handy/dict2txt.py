# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 05:00:14 2018

@author: stephen
"""

import json

def dict2json(dict_,filename):
    with open(filename, 'w') as file:
        string = json.dumps(dict_).replace(",", ",\n")
        file.write(string)
       
def json2dict(filepath):
    with open(filepath, 'r') as file:
        dictdump = json.loads(file.read())
        return dictdump
    return None

def dict2txt(dict_,filename):
    dict2json(dict_,filename)
    
def txt2dict(filepath):
    json2dict(filepath)
    
if __name__ == "__main__":
    dict2txt({'a':1,'b':2},'test.json')
    print(txt2dict('test.json'))