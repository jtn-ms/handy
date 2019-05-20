import os
import sys
import platform

from .constants import msg_file_not_found

import re

# IN: persistent_peers = "xxxx@yyy:dddd"
# OUT:persistent_peers = ""
def replaceKey(keystring,filename,quotechar='"',value=""):
    fullpath = os.path.realpath(filename)
    if not os.path.exists(fullpath): print(msg_file_not_found); return
    if not os.path.isfile(fullpath): print("directory not accepted."); return
    f = open(fullpath)
    output = []
    context = '{0}(.+?){1}'.format(quotechar,quotechar) if quotechar is '"' else "{0}(.+?){1}".format(quotechar,quotechar)
    emptyquotes = '{0}{1}'.format(quotechar,quotechar) if quotechar is '"' else "{0}{1}".format(quotechar,quotechar)
    template = '{0}%s{1}'.format(quotechar,quotechar) if quotechar is '"' else "{0}%s{1}".format(quotechar,quotechar)
    for line in f:
        if not line.startswith(keystring): output.append(line); continue
        if emptyquotes in line: output.append(line.replace(emptyquotes, template%value)); continue
        try: found = re.search(context, line).group(1)
        except: continue
        output.append(line.replace(found, value))
    f.close()
    f = open(fullpath, 'w')
    f.writelines(output)
    f.close()

def concatStr(filename,juncword=','):
    fullpath = os.path.realpath(filename)
    if not os.path.exists(fullpath): print(msg_file_not_found); return ""
    if not os.path.isfile(fullpath): print("directory not accepted."); return ""
    with open(fullpath) as lines:
        return juncword.join([line.strip('\n') for line in lines])

msg_help_clearkey = "Written by junying, 2019-05-20 \
                    \nUsage: replacekey [keystring] [filepath] [quotechar] [replacestring/replacefile] \
                    \nUsage: replacekey [keystring] [filepath] \
                    \nUsage: replacekey [keystring] [filepath] [quotechar] \
                    \nUsage: replacekey [keystring] [filepath] [replacestring/replacefile] \
                    \nDefault: replacekey [keystring] [filepath] '\"' \"\" "
                
def replconfkey():
    if len(sys.argv) < 3: print(msg_help_clearkey); return
    if len(sys.argv) == 3: replaceKey(sys.argv[1],sys.argv[2]); return
    if len(sys.argv[3]) > 1:
        replacestr = concatStr(sys.argv[3]) if os.path.isfile(sys.argv[3]) else sys.argv[3]
        replaceKey(sys.argv[1],sys.argv[2],'"',replacestr); return
    replacestr = sys.argv[4] if len(sys.argv) > 4 else ""
    if os.path.isfile(replacestr): replacestr = concatStr(replacestr)
    replaceKey(sys.argv[1],sys.argv[2],sys.argv[3],value)

msg_help_concatstr = "Written by junying, 2019-05-20 \
                     \nUsage: concatstr [filepath] [juncword] \
                     \nDefault: concatstr [filepath] ',' "
                      
def concatstr():
    if len(sys.argv) < 2: print(msg_help_clearkey); return
    juncword = ',' if len(sys.argv) == 2 else sys.argv[2]
    print(concatStr(sys.argv[1]))