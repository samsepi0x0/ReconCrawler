import requests
import sys
import random
import string

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def subdomains():
    website = input(color.BOLD + "Website: " + color.STOP)
    report = False
    rep = input(color.BOLD + "Generate Report? (Y/n): " +color.STOP)
    if rep == 'Y' or rep == 'y':
        report = True

    domains = open("subdomain_list.txt", 'r').readlines()
    print('\x1b[6;30;42m' + "[?] Subdomains Found: " + color.STOP)
    dom = list()
    for domain in domains:
        new_website = domain.strip() + "." + website
        try:
            r = requests.get("https://"+new_website)
            print(color.GREEN + "[+] " + color.STOP, new_website)
            dom.append(new_website)
        except:
            pass
    if report:
        try:
            url = random_string_generator(12, string.ascii_letters)
            with open("Report/subdomain_lookup_" + str(url) + ".txt" , 'w') as file:
                file.write("Subdomains: \n")
                for i in dom:
                    file.write(str(i))
                    file.write("\n")
            print(color.BLUE + "[+]Report Generated Successfully at Report/subdomain_lookup_" + str(url) + ".txt ." + color.STOP)
        except:
            print(color.RED + "[-]Error generating Report." + color.STOP)

#subdomains()