# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 18:04:48 2018

@author: stephen
"""
from __future__ import absolute_import

from handy.misc import switch
# this function temporarily works
# do not set environment variable permanently.
# https://docs.python.org/3/using/windows.html
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