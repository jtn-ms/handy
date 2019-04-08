import os
import pytest
from handy.crypto.encrypt import encrypt,decrypt

testtimes = 1000

from handy.random.passwd import randomPW

def test_times():
    for i in range(testtimes):
        test_str = randomPW(i + 5)
        assert decrypt(encrypt(test_str).encode('ascii', 'ignore')) == test_str