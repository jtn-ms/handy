from rlp.utils import encode_hex, decode_hex

def encode(str):
    return encode_hex(str)

def decode(hex):
    import sys
    if sys.version_info[0] == 2:
        return decode_hex(hex)
    else:
        return decode_hex(hex).decode("utf-8")