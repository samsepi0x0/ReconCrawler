import requests
import re
from bs4 import BeautifulSoup

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def user():
    count = 0
    username = str(input(color.BOLD + "Username: " + color.STOP))
    if chkfb(username) != None:
        print (color.GREEN + "[+] FaceBook Account Exists." + color.STOP)
        count += 1
    if chktwitter(username) != None:
        print (color.GREEN + "[+] Twitter Account Exists." + color.STOP)
        count += 1
    if chkgit(username) != None:
        print (color.GREEN + "[+] Github Account Exists. " + color.STOP)
        count += 1
    if count == 0:
        print (color.RED + "[-] Username %s not found on Facebook,Twitter And Github"%(user), color.STOP)


def chkfb(username):
    link1 = "https://facebook.com/" + username
    resp1 = requests.get(link1)
    status = BeautifulSoup(resp1.text, 'html.parser')
    if resp1.status_code == 200:
        return True
    else:
        return None

def chktwitter(username):
    link2 = "https://twitter.com/" + username
    resp2 = requests.get(link2)
    status = BeautifulSoup(resp2.text, 'html.parser')
    if resp2.status_code == 200:
        return True
    else:
        return None

def chkgit(username):
    link3 = "https://github.com/" + username
    resp3 = requests.get(link3)
    status = BeautifulSoup(resp3.text, 'html.parser')
    if resp3.status_code == 200:
        return True
    else:
        return None 