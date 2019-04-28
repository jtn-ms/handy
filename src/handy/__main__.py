
from __future__ import absolute_import, print_function, unicode_literals

import argparse
parser = argparse.ArgumentParser()

def main():
    parser.add_argument('-m','--mode', default='json', help='modes: json, document, hack, file, network (default: json)')
    parser.add_argument('-x','--func', default='delkey', help='functions: delkey,rmkey ...')
    parser.add_argument('-d','--data', default='', help='input data')
    parser.add_argument('-i','--inpath', default='', help='indicates input file path.')
    parser.add_argument('-o','--outpath', default='', help='indicates output file path.')
    args = parser.parse_args()
    from .misc import switch
    for mode in switch(args.mode):
        if mode('json'):
            for func in switch(args.func):
                from .json.handler import load,save
                from .dict.handler import delkey,rmempty
                if func('delkey'):
                    if not args.inpath: print('add filepath with -f/--filepath.')
                    if not args.data: print('add keyname to be deleted with -i/--input.')
                    if not args.outpath: args.outpath='output.json' 
                    data = load(args.inpath)
                    delkey(data,args.data)
                    rmempty(data,args.data)
                    save(args.outpath)
                    break
                if func():
                    print('type mode with -x or --func.\n \
                          modes: delkey, rmempty')
                    break
            break
        if mode():
            print('type mode with -m or --mode')
            break
    
if __name__ == "__main__":
    main()