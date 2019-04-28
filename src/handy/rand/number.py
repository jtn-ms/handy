# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:20:38 2017

@author: Frank
"""

from random import choice

#封装函数，生成随机手机号码
def randomPN():
  area_num = ['187','186','186','158','155','156','138','135','136','177','176','144','147']
  #获取手机号码区域号
  area_number = choice(area_num)

  #生成后8位手机号码
  seed = "1234567890"
  sa = []
  for i in range(8):
      sa.append(choice(seed))
  last_eightnumber = ''.join(sa)

  #拼接生成完整手机号码
  return area_number + last_eightnumber

if __name__ == "__main__":
    print(randomPN())