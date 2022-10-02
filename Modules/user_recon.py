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
    if chkfb(username) != False:
        print (color.GREEN + "[+] FaceBook Account Exists." + color.STOP)
        count += 1
    if chkreddit(username) != False:
        print (color.GREEN + "[+] Reddit Account Exists." + color.STOP)
        count += 1
    if chkgit(username) != False:
        print (color.GREEN + "[+] Github Account Exists. " + color.STOP)
        count += 1
    if chktwitter(username) != False:
        print (color.GREEN + "[+] Twitter Account Exists. " + color.STOP)
        count += 1
    if count == 0:
        print (color.RED + "[-] Username %s not found on Facebook, Reddit, Github or Twitter"%(username), color.STOP)


def chkfb(username):
    link1 = "https://facebook.com/" + username
    resp1 = requests.get(link1)
    status = BeautifulSoup(resp1.text, 'html.parser')
    if resp1.status_code == 200:
        return True
    else:
        return False

def chkreddit(username):
    link2 = "https://www.reddit.com/user/" + username
    resp2 = requests.get(link2,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})
    status = BeautifulSoup(resp2.content, 'html.parser')
    for item in status.find_all('img'):
        if item['src'] == "https://www.redditstatic.com/desktop2x/img/snoomoji/snoo_thoughtful.png":
            return False
    return True

def chkgit(username):
    link3 = "https://github.com/" + username
    resp3 = requests.get(link3)
    status = BeautifulSoup(resp3.text, 'html.parser')
    if resp3.status_code == 200:
        return True
    else:
        return False 

def chktwitter(username):
    link4 = "https://twitter.com/" + username
    resp4 = requests.get(link4,headers={'User-Agent': 'APIs-Google (+https://developers.google.com/webmasters/APIs-Google.html)'})
    status = BeautifulSoup(resp4.text, 'html.parser')
    if status.find_all('html',{'class':"dog"}):
        return False
    return True

#user()
