# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:55:40 2018

@author: Frank

ref:https://www.dotnetperls.com/7-zip-examples
"""

import subprocess
import argparse
import os

paths = [
       "C:\\Program Files\\7-Zip\\7z.exe",
       "C:\\Program Files (x86)\\7-Zip\\7z.exe"
       ]
_7z = None
for path in paths:
    if os.path.exists(path):
        _7z = path
        break
def compress(files=None):
    if not _7z:
        print('Please install 7z first!')
        return
    filename = input('Enter filename:')
    pw = input('Enter password:')
    vsz = input('Enter volumn size:')
    if not files:
        cmd = '%s a -t7z -p%s %s *.* -mhe -r -v%s'%(_7z,pw,filename,vsz)
        print(cmd)
        subprocess.call(cmd)#subprocess.call([_7z, 'a', pw, '-y', filename, "*.*"])
    else:
        subprocess.call([_7z, 'a', pw, '-y', filename, files])
    
#import os
def decompress():
    if not _7z:
        print('Please install 7z first!')
        return
    filename = input('Enter filename!')    
    if not os.path.exists(filename):
        print('No such a file exists!')
        return
    pw = input('Enter password!')
    dst =os.path.join(os.getcwd(),os.path.splitext(filename)[0])
    cmd = '%s x %s -o%s  -p%s -sdel'%(_7z,filename,dst,pw)
    subprocess.call(cmd)

def decompress_zip(filename):
    _7z = None
    for path in ["C:\\Program Files\\7-Zip\\7z.exe","C:\\Program Files (x86)\\7-Zip\\7z.exe"]:
        if os.path.exists(path):
            _7z = path
            break
    if not _7z:
        print('Please install 7z first!')
        return
    if not os.path.exists(filename):
        print('No such a file exists!')
        return
    dst = os.path.join(os.getcwd(),os.path.splitext(filename)[0])
    cmd = '%s x %s -o%s -sdel'%(_7z,filename,dst)
    subprocess.call(cmd)
    
def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument("square", help="display a square of a given number",type=int)
    parser.add_argument("-m","--mode", help="modes=['compress','decompress'], compressing files and decompressing", default='compress')
    #parser.add_argument("-i","--input", help="indicate a file to be processed")
    args = parser.parse_args()
    if 'compress' == args.mode:
        compress()
    elif 'decompress' == args.mode:
        decompress()
    '''
    if args.input:
        if 'compress' in args.mode:
            compress()
        elif 'decompress' in args.mode:
            decompress()
    else:
        print('choose a file please!')
    '''
if __name__ == "__main__":
    main()
    
'''
def test():
    cmd = ['7z', 'a', 'Test.7z', 'Test', '-mx9']
    sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    return sp
    
def decompress_(src='filename.7z',dst=os.getcwd()):
    print('enter password')
    pw=input()
    subprocess.call(r'"C:\Program Files (x86)\7-Zip\7z.exe" x %s -o %s -p %s'%(src,dst,pw))
    
#import os
import zipfile    
def decompress():
    print('enter filename')
    filename = input()    
    print('enter password')
    pw = input()
    zipfile.ZipFile(filename).extractall(pwd=pw)
'''