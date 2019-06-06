from sys import platform
import os,sys

msg_help_column = "Written by junying, 2019-05-09 \
                  \nUsage: column [index] \
                  \nUsage2: column [index] [filename] \
                  \nEx1: cat a.txt | column [index] \
                  \nEx2: column 1 a.txt "

def column():
    if len(sys.argv) < 2: print(msg_help_column); return
    if any(char not in string.digits for char in sys.argv[1]): return "index must be digits"
    if len(sys.argv) == 2 and sys.stdin.isatty(): print(msg_help_column);return
    index = int(sys.argv[1])
    if len(sys.argv) == 2:
        for line in sys.stdin:
            frags = line.split()
            if len(frags) >= index: print(frags[index-1])
    else: 
        if not os.path.exists(sys.argv[2]) or not os.path.isfile(sys.argv[2]): return msg_file_not_found
        with open(sys.argv[2]) as file:
            for line in file:
                frags = line.split()
                if len(frags) >= index: print(frags[index-1])
    return
                    
# def column():
#     if platform == "win32": return
#     if len(sys.argv) < 2: return msg_help_column
#     if any(char not in string.digits for char in sys.argv[1]): return "index must be digits"
#     simplecmd = "awk '{print $%sF}'"%sys.argv[1]
#     if len(sys.argv) == 2:
#         if sys.stdin.isatty(): print(msg_help_column); return 
#         os.system(simplecmd); return
#     if not os.path.exists(sys.argv[2]) or not os.path.isfile(sys.argv[2]): print(msg_file_not_found); return
#     os.system("cat {1} | {0}".format(simplecmd,sys.argv[2])) 

msg_help_colex = "Written by junying, 2019-06-06 \
                  \nUsage: colex [index] \
                  \nUsage2: colex [index] [filename] \
                  \nEx1: cat a.txt | colex [index] \
                  \nEx2: colex 1 a.txt "

def colex():
    if len(sys.argv) < 2: print(msg_help_colex); return
    if any(char not in string.digits for char in sys.argv[1]): return "index must be digits"
    if len(sys.argv) == 2 and sys.stdin.isatty(): print(msg_help_colex);return
    index = int(sys.argv[1])
    if len(sys.argv) == 2:
        for line in sys.stdin:
            frags = line.split()
            if len(frags) >= index: del frags[index-1]
            print("\t".join(frags))
    else:
        if not os.path.exists(sys.argv[2]) or not os.path.isfile(sys.argv[2]): return msg_file_not_found
        with open(sys.argv[2]) as file:
            for line in file:
                frags = line.split()
                if len(frags) >= index: del frags[index-1]
                print("\t".join(frags))
   
msg_help_row = "Written by junying, 2019-05-09 \
               \nUsage: row [index] \
               \nUsage2: row [index] [filename] \
               \nUsage3: row [index] [filename] [offset] \
               \nEx1: cat a.txt | row 1 \
               \nEx2: row 2 a.txt \
               \nEx3: row 3 a.txt 1"

from ._constants import msg_file_not_found

import string

def row():
    if len(sys.argv) < 2: print(msg_help_row);return
    if any(char not in string.digits for char in sys.argv[1]): return "index must be digits"
    if len(sys.argv) == 2 and sys.stdin.isatty(): print(msg_help_row);return
    if len(sys.argv) == 2: 
        for index,line in enumerate(sys.stdin):
            if index+1 == int(sys.argv[1]): print(line.strip('\n'));return
    elif len(sys.argv) == 3:
        if not os.path.exists(sys.argv[2]): return msg_file_not_found
        with open(sys.argv[2]) as file:
            for index, line in enumerate(file):
                if index+1 == int(sys.argv[1]): print(line.strip('\n'));return
    else:
        offset = int(sys.argv[3]) if all(char in string.digits for char in sys.argv[3]) else 0
        with open(sys.argv[2]) as file:
            for index, line in enumerate(file):
                if index+1 == int(sys.argv[1])+offset: print(line.strip('\n'));return
# def row():
#     if len(sys.argv) < 2: return msg_help_row
#     if any(char not in string.digits for char in sys.argv[1]): return "index must be digits"
#     if len(sys.argv) == 2 and sys.stdin.isatty(): return msg_help_row    
#     if platform == "win32": return "this function only support linux os. "
#     if len(sys.argv) == 2: os.system('sed -n "%sp"'%sys.argv[1]); return
#     if not os.path.exists(sys.argv[2]) or not os.path.isfile(sys.argv[2]): return msg_file_not_found
#     if len(sys.argv) == 3:
#         os.system('cat {1} | sed -n "{0}p"'.format(sys.argv[1],sys.argv[2]))
#     else:
#         offset = int(sys.argv[3]) if all(char in string.digits for char in sys.argv[3]) else 0
#         os.system('cat {1} | sed -n "{0}p"'.format(int(sys.argv[1])+offset,sys.argv[2]))

msg_help_colex = "Written by junying, 2019-06-06 \
                 \nUsage: rowex [index] \
                 \nUsage2: rowex [index] [filename] \
                 \nUsage3: rowex [index] [filename] [offset] \
                 \nEx1: cat a.txt | rowex 1 \
                 \nEx2: rowex 2 a.txt \
                 \nEx3: rowex 3 a.txt 1"

def rowex():
    if len(sys.argv) < 2: print(msg_help_colex);return
    if any(char not in string.digits for char in sys.argv[1]): return "index must be digits"
    if len(sys.argv) == 2 and sys.stdin.isatty(): print(msg_help_colex);return
    if len(sys.argv) == 2: 
        for index,line in enumerate(sys.stdin):
            if index+1 == int(sys.argv[1]): continue
            print(line.strip('\n'));
    elif len(sys.argv) == 3:
        if not os.path.exists(sys.argv[2]): return msg_file_not_found
        with open(sys.argv[2]) as file:
            for index, line in enumerate(file):
                if index+1 == int(sys.argv[1]): continue
                print(line.strip('\n'));
    else:
        offset = int(sys.argv[3]) if all(char in string.digits for char in sys.argv[3]) else 0
        with open(sys.argv[2]) as file:
            for index, line in enumerate(file):
                if index+1 == int(sys.argv[1])+offset: continue
                print(line.strip('\n'));

msg_help_findstr = "Written by junying, 2019-05-09 \
                   \nUsage: find [keystring] [path] \
                   \nDefault: find [keystring] ."
                
def findstr():
    if platform == "win32": return
    if len(sys.argv) < 2: print(msg_help_findstr); return
    cmd = 'grep -r "%s"'%sys.argv[1]
    if len(sys.argv) == 2: os.system(cmd); return
    for index in range(2,len(sys.argv)):
        cmd += " %s"%sys.argv[index]
    os.system(cmd)

msg_help_extractstr = "Written by junying, 2019-05-10 \
                      \nUsage: extractstr [startmark] [endmark] [string]\
                      \nUsage2: echo [string] | extractstr [startmark] [endmark] \
                      \nEx1: echo acdAAA12345ZZZ | extractstr AAA ZZZ \
                      \nEx2: extractstr AAA ZZZ acdAAA12345ZZZ\
                      \nReturn:  12345"

import re

# In1:  $ echo "sssssAAAddd" | extractstr sssss ddd
# In2:  $ extractstr sssss ddd sssssAAAddd
# Out:   AAA      
def extractstr():
    if len(sys.argv) < 3: print(msg_help_extractstr); return
    context = '{0}(.+?){1}'.format(sys.argv[1],sys.argv[2])
    if len(sys.argv) == 3:
        if sys.stdin.isatty(): print(msg_help_extractstr); return
        for line in sys.stdin:
            try: found = re.search(context, line).group(1)
            except: found = ''
            if found: print(found.strip('\n'))
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
        if sys.stdin.isatty(): print(msg_help_fromstr); return
        for line in sys.stdin:
            start = line.find(sys.argv[1]) + len(sys.argv[1])
            if start < len(line) and line.find(sys.argv[1]) > -1: print(line[start:].strip('\n'))
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
        if sys.stdin.isatty(): print(msg_help_endstr); return
        for line in sys.stdin:
            end = line.find(sys.argv[1])
            if end: print(line[:end].strip('\n'))
    else:
        end = sys.argv[2].find(sys.argv[1])
        if end: print(sys.argv[2][:end])
        else: print(line)

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
        if origin: print(origin.strip('\n'))
        
msg_help_lenstr = "Written by junying, 2019-05-10 \
                      \nUsage: lenstr [string] \
                      \nExample: lenstr 123456789 \
                      \nReturn: 9"

def lenstr():
    if len(sys.argv) < 2: print(msg_help_lenstr); return
    print(len(sys.argv[1]))

msg_help_upperstr = "Written by junying, 2019-05-10 \
                    \nUsage: upperstr [string] \
                    \nExample: upperstr abcdef \
                    \nReturn: ABCDEF"

def upperstr():
    if len(sys.argv) < 2: print(msg_help_upperstr); return
    print(sys.argv[1].upper())
    
msg_help_lowerstr = "Written by junying, 2019-05-10 \
                    \nUsage: lowerstr [string] \
                    \nExample: lowerstr ABCDEF \
                    \nReturn: abcdef"

def lowerstr():
    if len(sys.argv) < 2: print(msg_help_lowerstr); return
    print(sys.argv[1].lower())
    
msg_help_chkstdin = "Written by junying, 2019-05-23 \
                    \nUsage: chkstdin \
                    \nExample: echo 'hello heidi!'|chkstdin"

def chkstdin():
    if len(sys.argv) >= 2 or sys.stdin.isatty(): print(msg_help_chkstdin); return
    for line in sys.stdin:
        print(line.strip('\n'))