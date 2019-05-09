import platform
import os,sys

msg_help_column = "Written by junying, 2019-05-09 \
                    \nUsage: column [index]"
                    
def column():
    if platform == "win32": return
    if len(sys.argv) < 2: print(msg_help_column); return
    os.system("sed -n '%sp'"%sys.argv[1])
    
msg_help_row = "Written by junying, 2019-05-09 \
                \nUsage: row [index]"
                    
def row():
    if platform == "win32": return
    if len(sys.argv) < 2: print(msg_help_row); return
    os.system("awk '{print $%sF}'"%sys.argv[1])

msg_help_findstr = "Written by junying, 2019-05-09 \
                   \nUsage: find [keystring] [path] \
                   \nDefault: find [keystring] ."
                
def findstr():
    if platform == "win32": return
    if len(sys.argv) < 2: print(msg_help_findstr); return
    cmd = "grep -nr '%s'"%sys.argv[1]
    if len(sys.argv) == 2: os.system(cmd); return
    for index in range(2,len(sys.argv)):
        cmd += " %s"%sys.argv[index]
    os.system(cmd)
    