import sys

from handy.json.handler import load,save
from handy.dict.mixedict import isin

msg_no_output = "When outpath not indicated, it will use inputpath as default.\
                    Please Type y/n/p(Yes/No/Outpath):\n"
msg_not_found = "file doesn't exist or wrong file."
msg_help = "Written by junying, 2019-04-29 \
            \nUsage: chkey [keyname] [inpath]"
def main():
    if len(sys.argv) < 3: print(msg_help); return
    # load
    indata = load(sys.argv[2])
    if not indata: print(msg_not_found); return
    # process
    if not isin(indata,sys.argv[1]): print("no found!")
    else: print("found!!!")