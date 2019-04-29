# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:53:30 2018

@author: Frank
"""
# Best way to download files
# 1. list to text
# 2. open IDM
# 3. import text file
# 4. check all files to one directory
def list2txt(list_,filename):
    with open(filename, "w") as file:
        for line in list_:
            #file.write('%s\n'%line)
            file.write(str(line))
            file.write('\n')

def txt2list(filepath):
    import os
    if not os.path.exists(filepath):
        print('there is not such a file!')
        return None
    list_ = []
    with open(filepath, "r") as file:
        lines = file.readlines()
        for line in lines:
            item = line.split('\n')[0]
            list_.append(item)
            #print(item)
    return list_
    
if __name__ == "__main__":
    #from .download import models
    list2txt(['a','b'],'models.txt')
    print(txt2list('models.txt'))