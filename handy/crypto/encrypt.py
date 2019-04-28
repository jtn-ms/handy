# -*- coding: utf-8 -*-
"""
Created on Sun Apr 1 20:19:17 2018

@author: Frank
"""
from cryptography.fernet import Fernet

__len__ = 32
__base__ = '6DMTghVtI8MVfnIz_ok076SctSbxCMPb'
__encrypted_ = 'gAAAAABawEyDXZaAvKoBun6RzcgBzgyKS6H58mxbGfw-R51CpiYKlNNmGvPTFS0pGrOtTE-8CCy2uotOkCSiD-CYCBVnZs3YRg=='

#str2bytes
#str.encode(string)#bytes(string,"utf-8")
#byte2str
#bytes.decode()

import base64

def gen_key(key,flag=True,base=__base__):
    if flag:
        skey = (key+base)[:__len__]#N->32
    else:
        skey = (base+key)[len(key):]#N->32
    bkey = str.encode(skey)# 32->32
    code = base64.urlsafe_b64encode(bkey)# 32->44
    return code
    
def encrypt(origin='bey0nd', key='I@mTheG0d'):
    code = gen_key(key)
    f = Fernet(code)
    return f.encrypt(str.encode(origin)).decode()

def decrypt(encrypted=__encrypted_, key='I@mTheG0d'):
    try:
        base64.urlsafe_b64decode(encrypted)
    except:
        print('invalid token'); return
    code = gen_key(key)
    f = Fernet(code)
    from handy.conv.basics import byte2ascii
    return f.decrypt(byte2ascii(encrypted)).decode()

import os
def encrypt2file(origin=None,
                 key=None,
                 filename=None):
    if not origin:
        origin = input('Type String to be Encrypted:\n')
    if not key:
        key = input('Type Key:\n')
    if not filename:
        filename = input('Type FileName:\n')
    encrypted = encrypt(origin,key)
    fullpath = os.path.abspath(filename.replace("'",''))
    with open(fullpath,'w+b') as file:
        print(encrypted)
        file.write(str.encode(encrypted))

def decryptfromfile(filepath=None,
                    key=None):
    if not filepath:
        filepath = input('Type FileName:\n')
    if not key:
        key = input('Type Key:\n')
    fullpath = os.path.abspath(filepath.replace("'",''))
    if not os.path.exists(fullpath):
        print('There is no such a file')
        return
    fname,ext = os.path.splitext(os.path.split(fullpath)[1])
    encrypted = None
    with open(fullpath,'r+b') as file:
        line = file.read()
        if len(line) >= 100:
            encrypted = line if isinstance(line,str) else line.decode()
        elif len(fname) >= 100:
            encrypted = fname
    if encrypted:
        decrypted = decrypt(encrypted,key)
        print(decrypted)
        return decrypted
    
def test():
    encrypted = encrypt('IloveU',"Blowit")
    print(encrypted)
    decrypted = decrypt(encrypted,"Blowit")
    print(decrypted)

def test_fmode():
    encrypt2file('IloveU',"Blowit")
    decryptfromfile('ini','Blowit')
    
if __name__ == "__main__":
    #test()
    test_fmode()

    
