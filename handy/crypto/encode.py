from rlp.utils import encode_hex, decode_hex

def encode(str):
    return encode_hex(str)

def decode(hex):
    return decode_hex(hex)