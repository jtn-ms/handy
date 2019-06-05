import os, sys

msg_help_srm = "Written by junying, 2019-05-28 \
               \nUsage: srm [repeats] [path1] [path2] \
               \nExample: srm 10 big.file \
               \nDefault: srm 3 big.file \
               \nSame:    shred -fuvzn 10 big.file "

def secure_delete(filepath,repeats=3):
    os.system("shred -fuvzn {0} {1}".format(repeats,filepath))
    
from sys import platform
from ._file import findall
from ._constants import msg_file_not_found
import string

def srm():
    if platform == "darwin" or platform == "win32": print("linux os is required.");return
    if len(sys.argv) < 2: print(msg_help_srm); return
    repeats = 3
    #
    if all(char in string.digits for char in sys.argv[1]) and not os.path.exists(sys.argv[1]):
        repeats = sys.argv[1]
        paths = [sys.argv[index] for index in range(2,len(sys.argv)) if os.path.exists(sys.argv[index])]
    else: paths = [sys.argv[index] for index in range(1,len(sys.argv)) if os.path.exists(sys.argv[index])]
    # process
    for path in paths:
        if not os.path.exists(path): continue
        if os.path.isfile(path): print("processing %s"%path);secure_delete(path,repeats); continue
        for filepath in findall(path): print("processing %s"%filepath); secure_delete(filepath,repeats)