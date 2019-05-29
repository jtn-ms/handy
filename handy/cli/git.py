import os
import sys

msg_help = "Written by junying, 2019-04-30 \
            \nUsage: commit"
msg_comment = "enter comment: "
msg_not_found = "git repo not found"

cmd_add = "git add ."
cmd_comment = 'git commit -m "%s"'
cmd_push = "git push origin master"

def commit():
    if len(sys.argv) > 1: print(msg_help); return
    if '.git' not in os.listdir('.'): print(msg_not_found); print(msg_help); return
    comment = raw_input(msg_comment) if sys.version_info[0] == 2 else input(msg_comment)
    os.system(cmd_add)
    os.system(cmd_comment%comment)
    os.system(cmd_push)