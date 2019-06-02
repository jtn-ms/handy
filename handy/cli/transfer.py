import os
import sys

msg_help_upload = "Written by junying, 2019-04-30 \
                   \nUsage: upload [filename]"

from ._constants import msg_file_not_found

def upload():
    if len(sys.argv) < 2: print(msg_help_upload); return
    if not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]): print(msg_file_not_found); return
    os.system("curl --progress-bar --upload-file {0} https://transfer.sh/{1} | tee /dev/null".\
                                    format(sys.argv[1],os.path.split(sys.argv[1])[1]))
    os.system('echo')

msg_help_download = "Written by junying, 2019-04-30 \
                    \nUsage: download [filename] [password]"
                
def download():
    if len(sys.argv) < 3: print(msg_help_download); return
    os.system("wget https://transfer.sh/{1}/{0} | tee /dev/null".format(sys.argv[1],sys.argv[2]))
    