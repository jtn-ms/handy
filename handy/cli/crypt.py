import sys
import hashlib

msg_help_hash = "Written by junying, 2019-05-02 \
                \nUsage: hash [string] "                   
def hash():
    if len(sys.argv) < 2: print(msg_help_hash); return
    print(hashlib.sha224(sys.argv[1]).hexdigest())

from handy.crypto.encode import encode, decode

msg_help_encode = "Written by junying, 2019-05-02 \
                  \nUsage: encode [string] "    
                
def Encode():
    if len(sys.argv) < 2: print(msg_help_encode); return
    print(encode(sys.argv[1]))
    
msg_help_decode = "Written by junying, 2019-05-02 \
                  \nUsage: decode [string] "    
                
def Decode():
    if len(sys.argv) < 2: print(msg_help_decode); return
    print(decode(sys.argv[1]))
    
from handy.crypto.encrypt import encrypt,decrypt

msg_help_encrypt = "Written by junying, 2019-05-02 \
                  \nUsage: encrypt [string] [password] "    


from getpass import getpass
from ._constants import msg_passwd

def Encrypt():
    if len(sys.argv) < 2: print(msg_help_encrypt); return
    elif len(sys.argv) == 2: password = getpass(msg_passwd)
    else: password = sys.argv[2]
    print(encrypt(sys.argv[1],password))

msg_help_decrypt = "Written by junying, 2019-05-02 \
                  \nUsage: decrypt [string] [password] "   
                      
def Decrypt():
    if len(sys.argv) < 2: print(msg_help_decrypt); return
    elif len(sys.argv) == 2: password = getpass(msg_passwd)
    else: password = sys.argv[2]
    print(decrypt(sys.argv[1],password))

msg_help_genpass = "Written by junying, 2019-06-04 \
                   \nUsage: genpass [string] [level]"  

from handy.crypto.passcode import genpass
import string
def genpazz():
    if len(sys.argv) < 2: print(msg_help_genpass); return
    if len(sys.argv) == 2: return genpass(sys.argv[1])
    else: return genpass(sys.argv[1],int(sys.argv[2])) if all(char in string.digits for char in sys.argv[2]) else "level should be digital"