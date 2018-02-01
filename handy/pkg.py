# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 03:15:57 2018

@author: stephen
"""
import os

def get_upper(string,covers=['>','=','<']):
    for i,char in enumerate(string):
        if any(char is cover for cover in covers):
            return string[:i]
    return string
    
def download_pypi_pkgs(requires=['wget>=3.2']):
    for pkg in requires:
        pkg_name = get_upper(pkg)
        print('downloading %s...'%pkg_name)
        os.system('pip download %s'%pkg)
        
def install_pkgs(requires):
    for pkg in requires:
        pkg_name = get_upper(pkg)
        print('installing %s...'%pkg_name)
        os.system('pip install %s'%pkg)