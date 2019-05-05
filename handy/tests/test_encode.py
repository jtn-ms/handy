import os
from handy.crypto.encode import encode, decode

def test_genesis():
    assert(encode("testing") == "74657374696e67")
    assert(encode("god's color") == "676f64277320636f6c6f72")

from handy.rand.passwd import randomPW

def test_stress():
    count=1000
    for i in range(count):
        test_str = randomPW(i + 5)
        assert(decode(encode(test_str)) == test_str)