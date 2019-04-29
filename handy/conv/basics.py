import sys

def unicode2ascii(unistr):
    if sys.version_info[0] == 2: return unistr.encode('ascii', 'ignore')
    else: return unistr

def ascii2unicode(ascistr):
    if sys.version_info[0] == 2: return ascistr.decode()# or  unicode(ascistr)
    else: return ascistr

def byte2unicode(bytestr):
    return bytestr.decode()

def byte2ascii(bytestr):
    return str.encode(bytestr)