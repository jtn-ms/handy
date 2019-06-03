import os
import sys

msg_help_upload = "Written by junying, 2019-05-06 \
                   \nUsage: download [filename]"

from ._constants import msg_file_not_found

def download():
    if len(sys.argv) < 2: print(msg_help_upload); return
    if not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]): print(msg_file_not_found); return
    with open(sys.argv[1]) as file:
        for line in file:
            os.system('wget  %s'%line)