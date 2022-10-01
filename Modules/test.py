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
    if chkreddit(username) != False:
        print (color.GREEN + "[+] Reddit Account Exists." + color.STOP)
        count += 1
    if chkgit(username) != None:
        print (color.GREEN + "[+] Github Account Exists. " + color.STOP)
        count += 1
    if count == 0:
        print (color.RED + "[-] Username %s not found on Facebook, Reddit or Github"%(username), color.STOP)


def chkfb(username):
    link1 = "https://facebook.com/" + username
    resp1 = requests.get(link1)
    status = BeautifulSoup(resp1.text, 'html.parser')
    if resp1.status_code == 200:
        return True
    else:
        return None

def chkreddit(username):
    link2 = "https://www.reddit.com/user/" + username
    resp2 = requests.get(link2,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})
    status = BeautifulSoup(resp2.content, 'html.parser')
    for item in status.find_all('img'):
    #    print(item['src'])
        if item['src'] == "https://www.redditstatic.com/desktop2x/img/snoomoji/snoo_thoughtful.png":
            return False
    return True

    # if status.find_all('img') == True:
    #     return False
    # else:
    #     return True
#    if resp2.status_code == 200:
#        return True
#    else:
#        return None

def chkgit(username):
    link3 = "https://github.com/" + username
    resp3 = requests.get(link3)
    status = BeautifulSoup(resp3.text, 'html.parser')
    if resp3.status_code == 200:
        return True
    else:
        return None 
user()