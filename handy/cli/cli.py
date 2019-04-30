import sys
import argparse
parser = argparse.ArgumentParser()

msg_no_output = "When outpath not indicated, it will use inputpath as default.\n\
                 Please Type y/n/p(Yes/No/Outpath):\n"

def main():
    parser.add_argument('-m','--mode', default='json', help='modes: json, document, hack, file, network (default: json)')
    parser.add_argument('-x','--func', default='delkey', help='functions: delkey,rmkey ...')
    parser.add_argument('-d','--data', default='', help='input data')
    parser.add_argument('-i','--inpath', default='', help='indicates input file path.')
    parser.add_argument('-o','--outpath', default='', help='indicates output file path.')
    args = parser.parse_args()
    from handy.misc import switch
    for mode in switch(args.mode):
        if mode('json'):
            for func in switch(args.func):
                from handy.json.handler import load,save
                from handy.dict.mixedict import delkey,rmempty,isin
                if func('delkey'):
                    if not args.inpath: print('add input path with -i/--inpath.'); break
                    if not args.data: print('add keyname to be deleted with -d/--data.'); break
                    if not args.outpath:    
                        answer = raw_input(msg_no_output) if sys.version_info[0] == 2 else input(msg_no_output)
                        if 'y' in answer: args.outpath=args.inpath
                        elif 'n' in answer: break
                        else: args.outpath = answer
                    data = load(args.inpath)
                    if not data: print("input file doesn't exist or wrong file."); break
                    delkey(data,args.data); rmempty(data); save(data,args.outpath)
                    break
                if func():
                    print('type mode with -x or --func.\n \
                          modes: delkey, rmempty')
                    break
            break
        if mode():
            print('type mode with -m or --mode')
            break