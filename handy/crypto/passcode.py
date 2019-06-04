# level 1
origin_l0 ='0123456789abciloqszABES@'
crypted_l0='olzEAsb>&q@6<!10952483$a'
# level 1
origin_l1 ='0123456789abciloqstzABEHDOS#@'
crypted_l1='olzEAsb>&q@6<!1095+2483#OD$Ha'
# level 2
origin_l2 ='0123456789abcifhlmnoqrstvwxzABEFDHIMOSW_-^'
crypted_l2='olzEAsb>&q@6<!Fr1wu09h5+^mc2483fO#HWD$M-_v'

def genpass(string,level=0):
    from handy.misc import switch
    for depth in switch(level):
        if depth(0):
            origin = origin_l0
            crypted = crypted_l0
            break
        if depth(1):
            origin = origin_l1
            crypted = crypted_l1
            break
        if depth(2):
            origin = origin_l2
            crypted = crypted_l2
            break
        if depth():
            origin = origin_l1
            crypted = crypted_l1
            break
    result = ''
    for i,char in enumerate(string):
        result += crypted[origin.index(char)] if char in origin else char
    return result