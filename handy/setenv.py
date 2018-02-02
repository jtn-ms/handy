# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:04:48 2018

@author: stephen
"""
from .misc import switch
def set_env_variable(key,value,mode='add'):
    import os
    import platform
    if key in os.environ.keys() and 'add' in mode:
        for case in switch(platform.system()):
            if case('Windows'):
                if str(value) not in os.environ[key]:
                    os.environ[key] = os.environ[str(key)] + ';' + str(value)
                break
            if case('Linux'):
                break
            if case('MacOS'):
                break
    else:
        os.environ[key] = str(value)