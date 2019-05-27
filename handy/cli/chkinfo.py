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

msg_help_mac = "Written by junying, 2019-05-27 \
              \nUsage: mac [netipaddr]/[ipaddr] \
              \nEx1: mac 192.168.10.0/24 \
              \nEx2: mac 192.168.10.79"
                       
def mac():
    if len(sys.argv) < 2: print(msg_help_mac); return
    if "/" in sys.argv[1]: cmd="nmap -nsP %s | awk '/Nmap scan report/{printf $5;printf \" \";getline;getline;print $3;}'"%sys.argv[1]
    else: cmd = "nmap -nsP %s | awk '/Nmap scan report/{5;printf \"\";getline;getline;print $3;}'"%sys.argv[1]
    os.system(cmd)