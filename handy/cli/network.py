import platform
import os,sys

msg_help_mac = "Written by junying, 2019-05-17 \
               \nUsage: mac [iprange/mask] [targetip]\
               \nExample: mac 192.168.20.0/24 192.168.20.19"
                    
def column():
    if platform == "win32": return
    if len(sys.argv) < 2: print(msg_help_mac); return
    os.system("awk '{print $%sF}'"%sys.argv[1])