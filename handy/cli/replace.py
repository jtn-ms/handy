import sys, os

msg_help = "Written by junying, 2019-04-29 \
            \nUsage: repl [fromstr] [tostr] [file1] [file2] ..."
# python version of shell command replace
def main():
    if len(sys.argv) <= 3: print(msg_help); return
    files = [sys.argv[index] for index in range(3,len(sys.argv)) if os.path.exists(sys.argv[index]) and os.path.isfile(sys.argv[index])]
    cmd = "sed -i s/{0}/{1}/g ".format(sys.argv[1],sys.argv[2])
    for file in files:
        cmd += "%s "%file
    os.system(cmd)