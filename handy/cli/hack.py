import os,sys

msg_help_wifipass = "Written by junying, 2019-06-11 \
                    \nUsage: wifipass --help\
                    \nUsage: wifipass [access-point-name]\
                    \nTip: need administration privilege\
                    \nWindows:netsh wlan show profile name=[AP-Name] key=clear|findstr Key\
                    \nLinux: grep psk= /etc/NetworkManager/system-connections/*\
                    \nMacOS: security find-generic-password -wa labnol"

def wifipass():
    if len(sys.argv) > 1 and '-h' in sys.argv[1]: return msg_help_wifipass
    from handy.misc import switch
    for platform in switch(sys.platform):
        if platform("win32"):
            os.system('netsh wlan show profile name=%s key=clear|findstr Key'%sys.argv[1])
            break
        if platform("linux2"):
            os.system('grep psk= /etc/NetworkManager/system-connections/*')
            break
        if platform('osx'):
            os.system('security find-generic-password -wa labnol')
            break
        if platform():
            os.system('grep psk= /etc/NetworkManager/system-connections/*')
            break