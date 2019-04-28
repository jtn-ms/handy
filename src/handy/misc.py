# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 18:01:09 2017

@author: Frank
"""

from __future__ import absolute_import

import os,sys

def remove_all_files_with_certain_extension(dirpath,extension=".docx"):
    for filename in [ filename for filename in os.listdir(dirpath) if filename.endswith(extension)]:
        os.remove(os.path.join(dirpath, filename))

import glob

def remove_all_files_with_certain_pattern(dirpath,pattern="*.*"):
    for filepath in glob.glob(os.path.join(dirpath, pattern)):
        os.remove(filepath)

#import shutil
        
def mkdir(dirpath):
    if os.path.exists(dirpath):
        remove_all_files_with_certain_pattern(dirpath)
        #shutil.rmtree(dirpath)
        #os.mkdir(dirpath)
    else:
        os.mkdir(dirpath)

import webbrowser
import platform

def open_chrome(filepath):
    chrome_path = None
    for case in switch(platform.system()):
        if case('Windows'):
            for fullpath in ["C:/Program Files (x86)/Google/Chrome/Application/chrome.exe","C:/Program Files/Google/Chrome/Application/chrome.exe"]:
                if os.path.exists(fullpath):
                    chrome_path = fullpath + " %s"#'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
                    break
            break
        if case('MacOS'):
            print('MacOS code not steady. No exception handling')
            chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
            break
        if case('Linux'):
            if os.path.exists('/usr/bin/google-chrome'):
                chrome_path = '/usr/bin/google-chrome %s'
            break
    if chrome_path:
        print(chrome_path,filepath)
        webbrowser.get(chrome_path).open(filepath)#("http://bing.com")
    else:
        webbrowser.open(filepath)

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

# usage:
#            for case in switch(position):
#                if case('法人'):
#                    positions = ['项目经理']
#                    break
#                if case():
#                    positions = [position]
#                    break
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False
        
def sorted_keys(dictionary):
    keys = sorted(dictionary, key=dictionary.__getitem__)
    return keys

def reverse_dic(dic):
    return {v: k for k, v in dic.items()}


#if sys.version[0] > 2:
#    from inspect import getframeinfo,stack#,currentframe
#    def log(*arg):
#        caller = getframeinfo(stack()[1][0])
#        try:
#            print(*arg,'in line %d,%s'%(caller.lineno,os.path.split(caller.filename)[1]))
#        except:
#            pass
#        #frameinfo = getframeinfo(currentframe())
#        #print(*arg,'in line %d,%s'%(frameinfo.lineno,frameinfo.filename))
#else:
#    pass

