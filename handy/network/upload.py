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
    if not repo_path:
        print('decrypting failed')
        return
    from sys import platform
    if platform == "linux" or platform == "linux2":
        os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
    elif platform == "darwin":
        pass
    elif platform == "win32":
        os.system("start /B start cmd.exe @cmd /k ")
    import pyautogui
    pyautogui.typewrite('git clone %s'%repo_path,interval=0.01)
    pyautogui.press('enter')

def upload_repo():
    comment = input('Type Comment:\n')
    os.system('git add .')
    os.system('git commit -m %s'%comment)
    os.system('git push origin master')
    
def main():
    pass
    
if __name__ == '__main__':
	main()