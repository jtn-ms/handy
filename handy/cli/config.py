import os
import sys
import platform

from ._constants import msg_file_not_found

import re

# IN: persistent_peers = "xxxx@yyy:dddd"
# OUT:persistent_peers = ""
# or
# IN: persistent_peers = ""
# OUT:persistent_peers = "xxxx@yyy:dddd"
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

# IN:  persistent_peers = "xxxx@yyy:dddd,aaaa@bbb:ccc"
# OUT: persistent_peers = "aaaa@bbb:ccc"
# IN:  pex = true
# OUT: pex = false
def replaceValue(filename,keystring,srcstr,deststr="",sepchar=','):
    fullpath = os.path.realpath(filename)
    if not os.path.exists(fullpath): print(msg_file_not_found); return
    if not os.path.isfile(fullpath): print("directory not accepted."); return
    
    output = []
    f = open(fullpath)
    for line in f:
        if not line.startswith(keystring) or srcstr not in line: output.append(line); continue
        for template in ["{0}{1}","{1}{0}","{1} {0}","{0}"]:
            candidate = template.format(srcstr,sepchar)
            if candidate in line: 
                replace_string = template.format(deststr,sepchar) if deststr else ""
                output.append(line.replace(candidate, replace_string)); break
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
                    \nUsage: replconfkey [keystring] [filepath] [quotechar] [replacestring/replacefile] \
                    \nClean: replconfkey [keystring] [filepath] \
                    \nClean: replconfkey [keystring] [filepath] [quotechar] \
                    \nFillIn: replconfkey [keystring] [filepath] [replacestring/replacefile] \
                    \nDefault: replconfkey [keystring] [filepath] '\"' \"\" "
                
def replconfkey():
    if len(sys.argv) < 3: print(msg_help_clearkey); return
    if len(sys.argv) == 3: # process in default mode, clean not replace
        replaceKey(sys.argv[1],sys.argv[2]); return
    if len(sys.argv[3]) > 1: # if third param is not quotechar but replaceX
        replacestr = concatStr(sys.argv[3]) if os.path.isfile(sys.argv[3]) else sys.argv[3]
        replaceKey(sys.argv[1],sys.argv[2],'"',replacestr); return
    else: # if third param is quotechar
        if len(sys.argv) == 4: replaceKey(sys.argv[1],sys.argv[2],sys.argv[3]); return
        replacestr = sys.argv[4] if not os.path.isfile(sys.argv[4]) else concatStr(sys.argv[4])
        replaceKey(sys.argv[1],sys.argv[2],sys.argv[3],replacestr)

msg_help_concatstr = "Written by junying, 2019-05-20 \
                     \nUsage: concatstr [juncword] [filepath] \
                     \nUsage: concatstr [juncword] [str1] [str2] [str3] ...\
                     \nDefault: concatstr [filepath] "
                      
def concatstr():
    if len(sys.argv) < 2: print(msg_help_concatstr); return
    elif len(sys.argv) == 2: print(concatStr(sys.argv[1])); return
    elif len(sys.argv) == 3: print(concatStr(sys.argv[2],sys.argv[1])); return
    else: strlist=[sys.argv[index].strip('\r') for index in range(2,len(sys.argv))]; print(sys.argv[1].join(strlist)); return
    
    
msg_help_replconfval =  "Written by junying, 2019-05-20 \
                        \nUsage: replconfval [filepath] [keystring]  [findstr] [replacestr] [seperator] \
                        \nReplace: replconfval [filepath] [keystring]  [findstr] [replacestr] \
                        \nClean: replconfval [filepath] [keystring] [findstr] \
                        \nDefault: replconfval [filepath] [keystring]  true false ',' "
                
def replconfval():
    if len(sys.argv) < 4: print(msg_help_replconfval); return
    elif len(sys.argv) == 4: replaceValue(sys.argv[1],sys.argv[2],sys.argv[3]); return
    elif len(sys.argv) == 5: replaceValue(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]); return
    else: replaceValue(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]); return