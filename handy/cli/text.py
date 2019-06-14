import sys
import os

from ._constants import msg_file_not_found

def deleteLine(keystring,filename):
    fullpath = os.path.realpath(filename)
    if not os.path.exists(fullpath): print(msg_file_not_found); return
    if not os.path.isfile(fullpath): print("directory not accepted."); return
    f = open(fullpath)
    output = []
    for line in f:
        if not line.startswith(keystring):
            output.append(line)
    f.close()
    f = open(fullpath, 'w')
    f.writelines(output)
    f.close()

msg_help_deline = "Written by junying, 2019-04-29 \
                   \nUsage: deline [keystring] [filename]"

def deline():
    if len(sys.argv) < 3: print(msg_help_deline); return
    deleteLine(sys.argv[1],sys.argv[2])
    
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
    if len(sys.argv) <= 3: print(msg_help_replace); return
    paths = [sys.argv[index] for index in range(3,len(sys.argv)) if os.path.exists(sys.argv[index]) and os.path.isfile(sys.argv[index])]
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
        for line in sys.stdin: num += 1
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