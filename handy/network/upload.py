# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:26:46 2018

@author: Frank
"""

from handy.crypto.encrypt import decryptfromfile

import os
def download_repo():
    key = input('Type Key:\n')
    repo = input('Load Repo File:\n')
    repo_path = decryptfromfile(repo,key)
    os.system('git clone %s'%repo_path)

def upload_repo():
    comment = input('Type Comment:\n')
    os.system('git add .')
    os.system('git commit -m %s'%comment)
    os.system('git push origin master')
    
def main():
    pass
    
if __name__ == '__main__':
	main()