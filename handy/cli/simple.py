import os,sys
from sys import platform

def shutdown():
    if platform == "win32": os.system("shutdown /s /t 0")
    os.system("shutdown -h now")

def clear():
    if platform == "win32": os.system("cls"); return
    os.system("clear")
    
def openbashrc():
    if platform == "win32": return
    os.system("vim ~/.bashrc")
    
def sourcebashrc():
    if platform == "win32": return
    os.system(". ~/.bashrc")

msg_info = "type keystring: "

def chkbashrc():
    if platform == "win32": return
    if len(sys.argv) < 2: keystring = raw_input(msg_info) if sys.version_info[0] == 2 else input(msg_info)
    else: keystring = sys.argv[1]
    os.system('cat ~/.bashrc|grep %s'%keystring)