# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 15:01:06 2018

@author: Frank
"""

import os,glob

def get_subfolders_in_certain_depth(path=os.getcwd(),depth=1):
    subdirs = []
    for root,dirs,files in os.walk(path, topdown=True):
        depth_ = root[len(path) + len(os.path.sep):].count(os.path.sep)
        if depth_ == depth:
            # We're currently two directories in, so all subdirs have depth 3
            subdirs += [os.path.join(root, d) for d in dirs]
            dirs[:] = [] # Don't recurse any deeper
    return subdirs

def get_subdirs_by_glob(path=os.getcwd(),depth=1):
    files = glob.glob(os.path.join(path,'\\'.join('*'*depth)))
    dirs = filter(lambda f: os.path.isdir(f), files)
    return list(dirs)

def get_files(path,names,exts=['.jpg','.jpeg']):
    files = []
    for name in names:
        files_ = []
        for ext in exts:
            files_ += list(glob.iglob(path+'\\**\\' + '*'+name+'*'+ext, recursive=True))
        files += files_
    return files 