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

msg_help = "Written by junying, 2019-04-29 \
            \nUsage: deline [keystring] [filename]"

def main():
    if len(sys.argv) < 3: print(msg_help); return
    deleteLine(sys.argv[1],sys.argv[2])