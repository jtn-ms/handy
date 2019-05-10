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

msg_help_extractstr = "Written by junying, 2019-05-10 \
                      \nUsage: extractstr [startmark] [endmark] [string]\
                      \nExample: extractstr AAA ZZZ acdAAA12345ZZZ\
                      \nReturn:  12345"

import re

# In1:  $ echo "sssssAAAddd" | extractstr sssss ddd
# In2:  $ extractstr sssss ddd sssssAAAddd
# Out:   AAA      
def extractstr():
    if len(sys.argv) < 3: print(msg_help_extractstr); return
    context = '{0}(.+?){1}'.format(sys.argv[1],sys.argv[2])
    if len(sys.argv) == 3:
        for line in sys.stdin:
            try: found = re.search(context, line).group(1)
            except: found = ''
            if found: print(found)
    else:
        try: found = re.search(context, sys.argv[3]).group(1)
        except: found = ''
        if found: print(found)       

msg_help_fromstr = "Written by junying, 2019-05-10 \
                    \nUsage: fromstr [startmark] [string]\
                    \nExample: fromstr AAA AbcAAAvcd \
                    \nReturn:  vcd"

# In1:  $ echo "sssssAAAddd" | fromstr AAA
# In2:  $ fromstr AAA sssssAAAddd
# Out:   ddd       
def fromstr():
    if len(sys.argv) < 2: print(msg_help_fromstr); return
    elif len(sys.argv) == 2:
        for line in sys.stdin:
            start = line.find(sys.argv[1]) + len(sys.argv[1])
            if start < len(line): print(line[start:])
    else:
        start = sys.argv[2].find(sys.argv[1]) + len(sys.argv[1])
        if start < len(sys.argv[2]): print(sys.argv[2][start:])
        
msg_help_endstr = "Written by junying, 2019-05-10 \
                      \nUsage: endstr [endmark] [string] \
                      \nExample: endstr AAA abcdeAAA\
                      \nReturn:  abcde"

# In1:  $ echo "sssssAAAddd" | endstr AAA
# In2:  $ endstr AAA sssssAAAddd
# Out:   sssss                          
def endstr():
    if len(sys.argv) < 2: print(msg_help_fromstr); return
    elif len(sys.argv) == 2:
        for line in sys.stdin:
            end = line.find(sys.argv[1])
            if end: print(line[:end])
    else:
        end = sys.argv[2].find(sys.argv[1])
        if end: print(sys.argv[2][:end])

msg_help_excludestr = "Written by junying, 2019-05-10 \
                      \nUsage: excludestr [excludestring1] \
                      \nExample: excludestr AAA "

# In:  $ echo "sssssAAAddd" | excludestr AAA ddd
# Out:   sssss
def excludestr():
    if len(sys.argv) < 2: print(msg_help_excludestr); return
    strlist = [sys.argv[index] for index in range(1,len(sys.argv))]
    for line in sys.stdin:
        origin = line
        for keystr in strlist:
            origin = origin.replace(keystr, '')
        if origin: print(origin)
        
msg_help_lenstr = "Written by junying, 2019-05-10 \
                      \nUsage: lenstr [string] \
                      \nExample: lenstr AAA \
                      \nReturn: 3"

# In:  $ lenstr 123456789
# Out:   9               
def lenstr():
    if len(sys.argv) < 2: print(msg_help_lenstr); return
    print(len(sys.argv[1]))