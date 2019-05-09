# written by junying
# 2019-04-29
# dict + list
#
# ex:
# mixed = {1:11,2:22,3:{1:111,2:222,3:333},4:[{1:1111,2:2222},{1:1,2:2}]}
#
def delkey(mixed,field):
    if isinstance(mixed,dict):        
        for key, value in mixed.items():
            if key == field: mixed.pop(field)
            if isinstance(value, dict) or isinstance(value, list): delkey(value,field)
    elif isinstance(mixed, list) and all(isinstance(item,dict) for item in mixed):
        for item in mixed: delkey(item,field)                

def findkey(mixed,field):
    values = []
    if isinstance(mixed,dict):
        for key, value in mixed.items():
            if key == field: values.append(value)
            if isinstance(value, dict) or isinstance(value, list):
                for v in findkey(value,field): values.append(v)
    elif isinstance(mixed, list) and all(isinstance(item,dict) for item in mixed):
        for item in mixed: 
            for v in findkey(item,field): values.append(v)
    return values

def rmempty(mixed):
    if isinstance(mixed,dict):
        for key, value in mixed.items():
            if not value: mixed.pop(key)
            if isinstance(value, dict) or isinstance(value, list): rmempty(value)
    elif isinstance(mixed, list) and all(isinstance(item,dict) for item in mixed):
        for item in mixed: rmempty(item)

def isin(mixed,field):
    count = 0
    if isinstance(mixed,dict):
        for key, value in mixed.items():
            if key == field: count+=1
            if isinstance(value, dict) or isinstance(value, list): count+=isin(value,field)
    elif isinstance(mixed, list) and all(isinstance(item,dict) for item in mixed):
        for item in mixed: count+=isin(item,field)
    return count