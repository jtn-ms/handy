import sys

from handy.json.handler import load,save
from handy.dict.mixedict import rmempty

msg_no_output = "When outpath not indicated, it will use inputpath as default.\n \
                 Please Type y/n/p(Yes/No/Outpath):\n"
msg_not_found = "file doesn't exist or wrong file."
msg_help = "Written by junying, 2019-04-29 \
            \nUsage: rmempty [inpath] [outpath]"
def main():
    if len(sys.argv) < 2: print(msg_help); return
    elif len(sys.argv) == 2:
        if sys.version_info[0] == 2: answer = raw_input(msg_no_output)
        else: answer = input(msg_no_output)
        if 'y' in answer: outpath=sys.argv[1]
        elif 'n' in answer: return
        else: outpath = answer
    else:
        outpath = sys.argv[2]
    # load
    indata = load(sys.argv[1])
    if not indata: print(msg_not_found); return
    # process
    rmempty(indata)
    # save
    save(indata,outpath)