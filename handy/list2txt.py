# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:53:30 2018

@author: Frank
"""

from .download import models

# Best way to download files
# 1. list to text
# 2. open IDM
# 3. import text file
# 4. check all files to one directory
def list2txt(list_,filename):
    with open(filename, "w") as text_file:
        for line in list_:
            text_file.write('%s\n'%line)
            
if __name__ == "__main__":
    list2txt(models,'models.txt')