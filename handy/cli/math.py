import os,sys

msg_help_sum = "Written by junying, 2020-01-15 \
                \nUsage: sumup [filename] \
                \nUsage2: cat xxxx|column 1|sumup"
    
def sum():
    if len(sys.argv) < 2 and sys.stdin.isatty(): print(msg_help_sum); return
    _sum_ = 0
    if len(sys.argv) < 2:
        for line in sys.stdin:
            try: value=float(line.strip('\n'))
            except: continue
            _sum_+=value
        print("%.4f"%_sum_);return
    if not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]): print(msg_help_sum)
    with open(os.path.abspath(sys.argv[1])) as lines:
        for line in lines:
            try: value=float(line.strip('\n'))
            except: continue
            _sum_+=value
        print("%.4f"%_sum_);return
 