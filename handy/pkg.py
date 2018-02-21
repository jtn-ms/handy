# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 03:15:57 2018

@author: stephen
"""

from __future__ import absolute_import

import os

def get_upper(string,covers=['>','=','<']):
    for i,char in enumerate(string):
        if any(char is cover for cover in covers):
            return string[:i]
    return string
    
def download_pypi_pkgs(requires=['wget>=3.2']):
    if not requires:
        return
    if isinstance(requires,list):
        for pkg in requires:
            pkg_name = get_upper(pkg)
            print('downloading %s...'%pkg_name)
            os.system('pip download %s'%pkg)
    elif isinstance(requires,dict):
        for key in requires.keys():
            print('downloading %s...'%key)
            os.system('pip download %s'%requires[key])        
        
def install_pypi_pkgs(requires):
    if not requires:
        return
    if isinstance(requires,list):
        for pkg in requires:
            pkg_name = get_upper(pkg)
            print('installing %s...'%pkg_name)
            os.system('pip install %s'%pkg)
    elif isinstance(requires,dict):
        for key in requires.keys():
            print('installing %s...'%key)
            os.system('pip install %s'%requires[key])            

def install_conda_pkgs(requires):
    if not requires:
        return
    if isinstance(requires,list):
        for pkg in requires:
            pkg_name = get_upper(pkg)
            print('installing %s...'%pkg_name)
            os.system('conda install %s'%pkg)
    elif isinstance(requires,dict):
        for key in requires.keys():
            print('installing %s...'%key)
            os.system('conda install %s'%requires[key])

def download_debi_pkg(requires):
    #https://stackoverflow.com/questions/4419268/how-do-i-download-a-package-from-apt-get-without-installing-it
    if not requires:
        return
    if isinstance(requires,list):
        for pkg in requires:
            pkg_name = get_upper(pkg)
            print('installing %s...'%pkg_name)
            os.system('apt-get -d install %s'%pkg)
    elif isinstance(requires,dict):
        for key in requires.keys():
            print('installing %s...'%key)
            os.system('apt-get -d install %s'%requires[key])
    print('chk->/var/cache/apt/archives')
            
def check_cache_dir():
    if 'LocalAppData' not in os.environ.keys():
        print('No windows! No LocalAppData!')
        return None
    for item in ['pip/Cache','conda/conda/pkgs']:
        path = os.path.join(os.environ['LocalAppData'],item)
        if os.path.exists(path):
            print(path)