import os,sys

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, _, filenames in os.walk(start_path):
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
    if "/" in sys.argv[1]: cmd='nmap -nsP %s | awk "/Nmap scan report/{printf $5;printf \" \";getline;getline;print $3;}"'%sys.argv[1]
    else: cmd = 'nmap -nsP %s | awk "/Nmap scan report/{5;printf \"\";getline;getline;print $3;}"'%sys.argv[1]
    os.system(cmd)
    
from ._file import findbyname
msg_help_version = "Written by junying, 2019-04-29 \
                    \nUsage: version [path]  \
                    \nDefault: version ."

def version():
    if len(sys.argv) < 2: dirpath='.'
    else: dirpath=sys.argv[1]
    equalstring = '='
    for filepath in findbyname('version',dirpath):
        with open(filepath, 'r') as file:
            for line in file:
                if equalstring in line and any(line.startswith(string) for string in ['__version__','_version_','version']):
                    version = line.strip().split('=')[1].strip(' \'"'); print(version); return
    print('not found!')

from handy.network.worm import get_private_ip,get_public_ip,get_gps,get_ipinfo

def pubip():
    return get_public_ip()

def privip():
    return get_private_ip()

def gps():
    return get_gps()

def ipinfo():
    return get_ipinfo()