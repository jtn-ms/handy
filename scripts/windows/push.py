# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 15:12:09 2017

@author: Frank
"""
def push(comment):
    #import subprocess as sub
    #sub.Popen('cmd /K dir')
    #sub.Popen(['cmd', '/K', 'dir'])
    
    #import pyautogui
    #pyautogui.typewrite('git add .')
    #pyautogui.keyDown('enter')
    #pyautogui.typewrite('git commit -m %s'%comment)
    #pyautogui.keyDown('enter')
    #pyautogui.typewrite('git push origin master')
    #pyautogui.keyDown('enter')
    
    import os
    os.system('git add .')
    os.system('git commit -m %s'%comment)
    os.system('git push origin master')

import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-b","--branch", help="branch=[master,old],select git branch")
    parser.add_argument("-c","--comment", help="leave comment please.")
    args = parser.parse_args()
    # checking out branch
    if args.branch:
        branch = args.branch
    else:
        branch = input('select git branch.\n')
    import os
    os.system('git fetch && git checkout %s'%branch)
    # pushing code
    if args.comment:
        push(args.comment)
    else:
        comment = input('leave comment please.\n')
        push(comment)

if __name__ == "__main__":
    main()