import sys

from handy.json.handler import load,save
from handy.dict.mixedict import isin, delkey,rmempty

msg_no_output = "When outpath not indicated, it will use inputpath as default.\
                    Please Type y/n/p(Yes/No/Outpath):\n"
msg_not_found = "file doesn't exist or wrong file."
msg_help_chkey = "Written by junying, 2019-04-29 \
                 \nUsage: chkey [keyname] [inpath]"
def chkey():
    if len(sys.argv) < 3: print(msg_help_chkey); return
    indata = load(sys.argv[2])
    if not indata: print(msg_not_found); return
    if not isin(indata,sys.argv[1]): print("no found!")
    else: print("found!!!")
    
msg_help_delkey = "Written by junying, 2019-04-29 \
                  \nUsage: delkey [key] [inpath] [outpath]"
def delkey():
    if len(sys.argv) < 3: print(msg_help_delkey); return
    elif len(sys.argv) == 3:
        answer = raw_input(msg_no_output) if sys.version_info[0] == 2 else input(msg_no_output)
        if 'y' in answer: outpath=sys.argv[2]
        elif 'n' in answer: return
        else: outpath = answer
    else: outpath = sys.argv[3]
    indata = load(sys.argv[2]); key = sys.argv[1]
    if not indata: print(msg_not_found); return
    delkey(indata,key); rmempty(indata); save(indata,outpath)
    
msg_help_rmempty = "Written by junying, 2019-04-29 \
                   \nUsage: rmempty [inpath] [outpath]"
            
def rmempty():
    if len(sys.argv) < 2: print(msg_help_rmempty); return
    elif len(sys.argv) == 2:
        answer = raw_input(msg_no_output) if sys.version_info[0] == 2 else input(msg_no_output)
        if 'y' in answer: outpath=sys.argv[1]
        elif 'n' in answer: return
        else: outpath = answer
    else: outpath = sys.argv[2]
    # load
    indata = load(sys.argv[1])
    if not indata: print(msg_not_found); return
    # process
    rmempty(indata)
    # save
    save(indata,outpath)