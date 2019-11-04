# -*- coding: utf-8 -*-
from sys import platform
import os,sys

if sys.version_info[0] == 3:
    from imp import reload

reload(sys)

if sys.version_info[0] == 2:
    sys.setdefaultencoding('utf-8')

msg_help_zh2ko = "Written by junying, 2019-10-31 \
                \nDescription: translate from chinese to korean. \
                \nUsage: zh2ko [text] \
                \nEx: zh2ko 内容 \
                \nReturn: 내용 "
                
from handy.youdao.zh2ko import YouDaoTranslate
def zh2ko():
    if len(sys.argv) == 1 and sys.stdin.isatty(): print(msg_help_zh2ko);return
    handler = YouDaoTranslate()
    if len(sys.argv) == 1:
        for line in sys.stdin:
            handler.translate(line.strip('\n'))
    else: 
        if not os.path.exists(sys.argv[1]) or not os.path.isfile(sys.argv[1]):
            handler.translate(sys.argv[1].strip('\n')); return
        with open(sys.argv[1]) as file:
            for line in file:
                handler.translate(line.strip('\n'))