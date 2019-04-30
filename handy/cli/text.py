import sys
import os

def deleteLine(keystring,filename):
    fullpath = os.path.realpath(filename)
    if not os.path.exists(fullpath): print("file doesn't exist."); return
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
                    \nUsage: repl [fromstr] [tostr] [file1] [file2] ..."
# python version of shell command replace
def replace():
    if len(sys.argv) <= 3: print(msg_help_replace); return
    files = [sys.argv[index] for index in range(3,len(sys.argv)) if os.path.exists(sys.argv[index]) and os.path.isfile(sys.argv[index])]
    cmd = "sed -i s/{0}/{1}/g ".format(sys.argv[1],sys.argv[2])
    for file in files:
        cmd += "%s "%file
    os.system(cmd)
    
def find(name, path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in file: return os.path.join(root, file)

msg_help_version = "Written by junying, 2019-04-29 \
                    \nUsage: version [path]  \
                    \nDefault: version ."

def version():
    if len(sys.argv) < 2: dirpath='.'
    else: dirpath=sys.argv[1]
    filepath = find('version',dirpath)
    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith('__version__') or line.startswith('_version_') or line.startswith('version'):
                version = line.strip().split('=')[1].strip(' \'"'); print(version); return
    print('not found!')

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
    for root, dirs, files in os.walk('.'):
        for file in files:
            if any(ext in os.path.splitext(file)[1] for ext in exts): count += filelines(os.path.join(root, file))
    print("lines: %d"%count)