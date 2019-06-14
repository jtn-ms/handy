import os
import sys
# curl --progress-bar --upload-file {0} https://transfer.sh/{1} | tee /dev/null
# wget https://transfer.sh/{1}/{0} | tee /dev/null
msg_help_upload = "Written by junying, 2019-04-30 \
                   \nUsage: upload [filename] \
                   \nUsage: upload [filename] --print\
                   \nUsage: upload [filename] --mail"

from ._constants import msg_file_not_found
import subprocess
from handy.hack.mail import send_mail
def upload():
    if len(sys.argv) < 2 or any(argv.startswith("-h") for argv in sys.argv): return msg_help_upload
    if not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]): return msg_file_not_found
    if any(argv.startswith('--mail') for argv in sys.argv): send_mail(files=[sys.argv[1]],subject=sys.argv[1])
    else:
        result = subprocess.check_output("curl --silent --progress-bar --upload-file {0} https://transfer.sh/{1}".\
                                        format(sys.argv[1],os.path.split(sys.argv[1])[1]),shell=True)
        if any(argv.startswith('--print') for argv in sys.argv): print(result)
        send_mail(subject=result)

msg_help_download = "Written by junying, 2019-04-30 \
                    \nUsage:  download \
                    \nUsage2: download -h"

from handy.hack.mail import read_email
def download():
    if any("-h" in argv for argv in sys.argv): return msg_help_download
    when,who,what=read_email()
    if not when or not who or not what: return "network connection not good."
    if 'olzs' not in who: return "no uploaded at present!"
    if 'https://transfer.sh' not in what: return
    os.system("wget --quiet {0} | tee /dev/null".format(what))
    