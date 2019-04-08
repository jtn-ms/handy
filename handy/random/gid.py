# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:48:14 2017

@author: Frank
"""

def getValidateCheckout(id17):
    '''获得校验码算法'''
    weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2] #十七位数字本体码权重   
    validate=['1','0','X','9','8','7','6','5','4','3','2'] #mod11,对应校验码字符值   

    sum=0
    mode=0
    for i in range(0,len(id17)):
        sum = sum + int(id17[i])*weight[i]
    mode=sum%11
    return validate[mode]

import random
import datetime

def randomDate(start="1960-01-01",end = "2000-12-30"):
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
    date = datetime.datetime.strftime(datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0,days)), "%Y%m%d")    
    return date

def randomGID(sex = 1):
    '''产生随机可用身份证号，sex = 1表示男性，sex = 0表示女性'''
    #地址码产生
    from addr import addr #地址码
    addrInfo = random.randint(0,len(addr))#随机选择一个值
    addrId = addr[addrInfo][0]
    addrName = addr[addrInfo][1]
    idNumber = str(addrId)
    #出生日期码
    birthDays = randomDate()
    idNumber = idNumber + str(birthDays)
    #顺序码
    for i in range(2):#产生前面的随机值
        n = random.randint(0,9)# 最后一个值可以包括
        idNumber = idNumber + str(n)
    # 性别数字码
    sexId = random.randrange(sex,10,step = 2) #性别码
    idNumber = idNumber + str(sexId)
    # 校验码
    checkOut = getValidateCheckout(idNumber)
    idNumber = idNumber + str(checkOut)
    return idNumber,addrName,addrId,birthDays,sex,checkOut

def extract_birthday(gid):
    if isinstance(gid,int):
        gid = str(gid)
    if len(gid) == 15:
        return datetime.datetime(int(gid[6:10]),\
                                 int(gid[10:12]),\
                                 int(gid[12:14]))#gid[6:14]
    else:
        return datetime.datetime(int(gid[6:10]),\
                                 int(gid[10:12]),\
                                 int(gid[12:14]))#gid[6:14]

def calculateAge(born):
    today = datetime.datetime.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, day=born.day-1)
    if birthday > today and isinstance(born,datetime.datetime):
        return today.year-born.year - 1
    else:
        return today.year - born.year

def calcAge(gid):
    return calculateAge(extract_birthday(gid))
    
if __name__ == "__main__":
    print(calcAge('610481197108046218'))#random_greencard_id())#calculate_age(datetime.datetime(1989,1,25))
    