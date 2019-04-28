# written by junying
# 2019-04-28

def delkey(dic,field):
    for key, value in dic.items():
        if key == field: dic.pop(field)
        if isinstance(value, dict): delkey(value,field)

def rmempty(dic):
    for key, value in dic.items():
        if not value: dic.pop(key)
        if isinstance(value, dict): delkey(value)   

def isin(dic,field):
    found = False
    for key, value in dic.items():
        if key == field: return True
        if isinstance(value, dict) and isin(value,field): return True
    return found
