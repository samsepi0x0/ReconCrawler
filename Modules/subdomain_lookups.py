import requests
import sys

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def subdomains():
    website = input(color.BOLD + "Website: " + color.STOP)

    domains = open("subdomain_list.txt", 'r').readlines()
    print('\x1b[6;30;42m' + "[?] Subdomains Found: " + color.STOP)
    for domain in domains:
        new_website = domain.strip() + "." + website
        try:
            r = requests.get("https://"+new_website)
            print(color.GREEN + "[+] " + color.STOP, new_website)
        except:
            pass