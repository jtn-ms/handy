import os,sys

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

msg_help_dirsize = "Written by junying, 2019-05-10 \
                    \nUsage: dirsize [path]"

# In:  $ dirsize
# Out:   623.1 kB
import humanize
def dirsize():
    if len(sys.argv) < 2: print(humanize.naturalsize(get_size())); return
    print(humanize.naturalsize(get_size(sys.argv[1])))