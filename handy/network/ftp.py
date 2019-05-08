# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:07:54 2018

@author: Frank
"""

import os

from ftplib import FTP

def upload_ftp(ip):
    ftp = FTP(ip)
    uname = input('USERNAME: ')
    pw = input('PASSWORD: ')
    ftp.login(uname,pw)
    #ftp.cwd('/Enter the directory here/')
    for fileordir in os.listdir():
        if os.path.isfile(fileordir) and '7z' in fileordir:
            print(fileordir)
            file = open(fileordir,'rb')                  # file to send
            ftp.storbinary('STOR %s'%fileordir, file)     # send the file
            file.close()                                    # close file and FTP
    ftp.quit()

import pysftp
def upload_sftp(ip):
    uname = input('USERNAME: ')
    pw = input('PASSWORD: ')
    srv = pysftp.Connection(host=ip, username=uname,
    password=pw,log="./temp/pysftp.log")
    with srv.cd('public'): #chdir to public
        srv.put(r'C:\Upload\README.md') #upload file to nodejs/
    
    # Closes the connection
    srv.close()

def upload(ip):
    upload_ftp(ip)
    
import urllib 
def download_urllib(ip,filename='a.txt',path='Upload'):
    urllib.urlretrieve('ftp://%s/%s/%s'%(ip,path,filename), filename)

def download_ftp(ip,filename):
    ftp = ftplib.FTP(ip)
    uname = input('USERNAME: ')
    pw = input('PASSWORD: ')
    ftp.login(uname,pw)
    #ftp.cwd('/Enter the directory here/')
    LocalFile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, LocalFile.write, 1024)
    ftp.quit()
    LocalFile.close()
    
def download(ip,filename):
    download_urllib(ip,filename)
    
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    #parser.add_argument("square", help="display a square of a given number",type=int)
    parser.add_argument("-m","--mode", help="modes=['upload','download'], uploading files to the server", default='upload')
    parser.add_argument("-i","--ip", help="indicate a server ip address", default='39.108.104.125')
    #parser.add_argument("-c","--count", help="repeat count. not set.", type=int, default=1)
    args = parser.parse_args()
    if 'upload' in args.mode:
        upload(args.ip)
    else:
        download(args.ip)