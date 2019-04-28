# written by junying
# 2019-04-28

def delkey(dict_,field):
    for key, value in dict_.items():
        if key == field: dict_.pop(field)
        if isinstance(value, dict): delkey(value,field)

def rmempty(dict_):
    for key, value in dict_.items():
        if not value: dict_.pop(key)
        if isinstance(value, dict): rmempty(value)   

def isin(dic,field):
    found = False
    for key, value in dic.items():
        if key == field: return True
        if isinstance(value, dict) and isin(value,field): return True
    return found
