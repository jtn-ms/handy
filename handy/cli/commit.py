import os
import sys

msg_help = ""
msg_comment = "enter comment: "

cmd_add = "git add ."
cmd_comment = "git commit -m %s"
cmd_push = "git push origin master"

def main():
    os.system(cmd_add)
    if sys.version_info[0] == 2: comment = raw_input(msg_comment)
    else: comment = input(msg_comment)
    os.system(cmd_comment%comment)
    os.system(cmd_push)