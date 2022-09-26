import requests
from bs4 import BeautifulSoup
import random
import string

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

def scraper(report=False):
    try:
        URL = input(color.BOLD + "Website: " + color.STOP)

        r =requests.get(URL)
        soup = BeautifulSoup(r.content, features="lxml")
        dir_links = {}
        i = 0
        for a in soup.find_all('a', href=True):
            t = a['href']
            if t.startswith("/"):
                s = t.rfind('/')
                dir_links[i] = t[:s]
                i += 1
            if t.startswith(URL):
                link = t[len(URL):]	
                index = link.rfind('/')
                dir_links[i] = link[:index]
            i += 1
        link_list = list(dir_links.values())
        link_list = list(dict.fromkeys(link_list))

        print('\x1b[6;30;42m' + "[+] "+ str(len(link_list)) + " Directories found at LEVEL 1!" + color.STOP)
        for x in link_list:
            print(color.GREEN + "\t --> ", x + color.STOP)
        if report:
            try:
                url = random_string_generator(12, string.ascii_letters)
                with open("Report/crawler_" + str(url) + "_report.txt", "w") as file:
                    for x in link_list:
                        file.write(x)
                        file.write("\n")
                print(color.BLUE + "[+] Report generated Successfully at : crawler_" + str(url) + "_report.txt" + color.STOP)
            except:
                print(color.RED + "[-] Unable to Generate report. Try again later." + color.STOP)
    except:
        print(color.RED + "[-] Exception Occured. Try Again later." + color.STOP)
        return None

#scraper(True)