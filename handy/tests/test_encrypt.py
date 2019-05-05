import os
from handy.crypto.encrypt import encrypt,decrypt

count = 1000

from handy.rand.passwd import randomPW
from handy.conv.basics import unicode2ascii
def test_stress():
    for i in range(count):
        test_str = randomPW(i + 5)
        assert(decrypt(unicode2ascii(encrypt(test_str))) == test_str)