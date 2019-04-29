import sys
import os

def deleteLine(keystring,filepath):
    if not os.path.exists(filepath): print("file doesn't exist.\n"); return
    if not os.path.isfile(filepath): print("directory not accepted.\n"); return
    f = open(filepath)
    output = []
    for line in f:
        if not line.startswith(keystring):
            output.append(line)
    f.close()
    f = open(filepath, 'w')
    f.writelines(output)
    f.close()

msg_help = "Written by junying, 2019-04-29 \n\
            Usage: deline [keystring] [filename]\n"

def main():
    if len(sys.argv) < 3: print(msg_help); return
    deleteLine(sys.argv[0],sys.argv[1])