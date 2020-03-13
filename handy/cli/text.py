import sys
import os

from ._constants import msg_file_not_found
from ..misc import switch
def deleteLine(keystring,filename,option='-a'):
    fullpath = os.path.realpath(filename)
    if not os.path.exists(fullpath): print(msg_file_not_found); return
    if not os.path.isfile(fullpath): print("directory not accepted."); return
    f = open(fullpath)
    output = []
    for line in f:
        for case in switch(sys.argv[2]):
            if case("-e"):
                if not line.endswith(keystring):  output.append(line); break
            if case("-s"):
                if not line.startswith(keystring):  output.append(line); break
            if case():
                if not keystring in line:  output.append(line); break
    f.close()
    f = open(fullpath, 'w')
    f.writelines(output)
    f.close()

msg_help_deline = "NAME \
                   \n    deline deletes lines in file or stdin \
                   \nUSAGE \
                   \n    deline [keystring] [filename] [options]\
                   \nOPTION \
                   \n   -a(default)  anywhere in line\
                   \n   -e           ends with \
                   \n   -s           starts with \
                   \nEXAMPLE \
                   \n    deline stake accounts.lst\
                   \n          remove all lines which start with 'stake' in accounts.lst \
                   \n    cat accounts.lst|deline stake \
                   \n          print lines which start with 'stake'"

def deline():
    if len(sys.argv) < 2: print(msg_help_deline); return
    elif len(sys.argv) == 2:
        if sys.stdin.isatty(): print(msg_help_deline); return
        for line in sys.stdin:
            if line.startswith(sys.argv[1]): print(line.strip("\n"))
        return
    elif len(sys.argv) == 3:
        if os.path.exists(sys.argv[2]): deleteLine(sys.argv[1],sys.argv[2]); return
        elif sys.stdin.isatty(): print(msg_help_deline); return
        from handy.misc import switch
        for line in sys.stdin:
            for case in switch(sys.argv[2]):
                if case("-e"):
                    if not line.endswith(sys.argv[1]): print(line.strip("\n")); break
                if case("-s"):
                    if not line.startswith(sys.argv[1]): print(line.strip("\n")); break
                if case():
                    if not sys.argv[1] in line: print(line.strip("\n")); break
    else:
        deleteLine(sys.argv[1],sys.argv[2],sys.argv[3])

msg_help_replace = "Written by junying, 2019-04-29 \
                    \nUsage: repl [fromstr] [tostr] [path1] [path2] ..."
                    
def replacefile(srcstring,deststring,filename):
    fullpath = os.path.realpath(filename)
    if not os.path.exists(fullpath): print(msg_file_not_found); return
    if not os.path.isfile(fullpath): print("directory not accepted."); return
    f = open(fullpath)
    output = []
    for line in f:
        if srcstring in line: output.append(line.replace(srcstring, deststring))
        else: output.append(line)    
    f.close()
    f = open(fullpath, 'w')
    f.writelines(output)
    f.close()

from ._file import findall
# python version of shell command replace
def replace():
    if len(sys.argv) < 3: print(msg_help_replace); return
    if len(sys.argv) == 3:
        for line in sys.stdin:
            print(line.replace(sys.argv[1],sys.argv[2]).strip('\n'))
    paths = [sys.argv[index] for index in range(3,len(sys.argv)) if os.path.exists(sys.argv[index])]
    for path in paths:
        if not os.path.exists(path): continue
        if os.path.isfile(path): replacefile(sys.argv[1],sys.argv[2],path)
        else: 
            for f in findall(path): replacefile(sys.argv[1],sys.argv[2],f)
    
def filelines(filepath):
    if not os.path.isfile(filepath): return 0
    return sum(1 for line in open(filepath))

msg_help_totalines = "Written by junying, 2019-04-29 \
                     \nUsage: totalines [ext1] [ext2] ...\
                     \nDefault: totalines py go cpp h java\
                     \nEx: totalines py"
                    
def totalines():
    if not os.path.exists('.git'): print("git repo not found"); return
    if len(sys.argv) < 2: print(msg_help_totalines); exts = ['py','go','cpp','h','java']
    else: exts = [sys.argv[index] for index in range(1,len(sys.argv))]
    count = 0
    for root, _, files in os.walk('.'):
        for file in files:
            if any(ext in os.path.splitext(file)[1] for ext in exts): count += filelines(os.path.join(root, file))
    print("lines: %d"%count)

msg_help_linecount = "Written by junying, 2019-05-17 \
                     \nUsage: linecount [filename] \
                     \nUsage2: cat xxxx | linecount"
    
def linecount():
    if len(sys.argv) < 2 and sys.stdin.isatty(): print(msg_help_linecount); return
    if len(sys.argv) < 2:
        num = 0
        for _ in sys.stdin: num += 1
        print(num);return
    if not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]): print(msg_file_not_found)
    print(filelines(sys.argv[1]))
 
msg_help_oneline = "Written by junying, 2019-06-13 \
                   \nUsage: oneline [filename] \
                   \nUsage2: cat xxxx | oneline"
                         
def oneline():
    if len(sys.argv) < 2 and sys.stdin.isatty(): print(msg_help_oneline); return
    merged = ''
    if len(sys.argv) < 2:
        for line in sys.stdin: merged += line.strip('\n')
    elif not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]): print(msg_file_not_found); return
    else:
        with open(sys.argv[1]) as file:
            for line in file: merged += line.strip('\n')
    print(merged);