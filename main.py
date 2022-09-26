import sys
import os
from Modules import is_domain_registered
from Modules import whois_info
from Modules import subdomain_lookups
from Modules import crawler
from Modules import dirbuster
from Modules import port_scanner
from Modules import shodan_set_key
from Modules import shodan_scan_host
from Modules import shodan_search
from Modules import user_recon
from Modules import api_info

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'
    BLUR = '\x1b[6;30;42m'

def banner():
    if sys.platform[:3] == "win":
        command = "cls"
    else:
        command = "clear"
    res = os.system(command)
    print("\n" + color.BLUE+"""     ____  _____ ____ ___  _   _   ____ ____      ___        ___     _____ ____  
    |  _ \| ____/ ___/ _ \| \ | | / ___|  _ \    / \ \      / / |   | ____|  _ \ 
    | |_) |  _|| |  | | | |  \| || |   | |_) |  / _ \ \ /\ / /| |   |  _| | |_) |
    |  _ <| |__| |__| |_| | |\  || |___|  _ <  / ___ \ V  V / | |___| |___|  _ < 
    |_| \_\_____\____\___/|_| \_(_)____|_| \_\/_/   \_\_/\_/  |_____|_____|_| \_\\""" + color.STOP)
    print()
    print ("    "+ "-"*77)
    print()

def banner_shodan():
    if sys.platform[:3] == "win":
        command = "cls"
    else:
        command = "clear"
    res = os.system(command)
    print("\n" + color.BLUE + """     ____  _   _       ____              
    / ___|| | | | ___ |  _ \  __ _ _ __  
    \___ \| |_| |/ _ \| | | |/ _` | '_ \ 
     ___) |  _  | (_) | |_| | (_| | | | |
    |____/|_| |_|\___/|____/ \__,_|_| |_|""" + color.STOP)
    print()
    print ("    "+ "-"*38)
    print()

def banner_web():
    if sys.platform[:3] == "win":
        command = "cls"
    else:
        command = "clear"
    res = os.system(command)
    print(color.BLUE + """    __        __   _           ____       ____            
    \ \      / /__| |__       |  _ \ ___ / ___|___  _ __  
     \ \ /\ / / _ \ '_ \ _____| |_) / _ \ |   / _ \| '_ \ 
      \ V  V /  __/ |_) |_____|  _ <  __/ |__| (_) | | | |
       \_/\_/ \___|_.__/      |_| \_\___|\____\___/|_| |_|""" + color.STOP)
    print()
    print ("    "+ "-"*57)
    print()

def banner_dns():
    if sys.platform[:3] == "win":
        command = "cls"
    else:
        command = "clear"
    res = os.system(command)

    print(color.BLUE + """     ____  _   _ ____        _____                       
    |  _ \| \ | / ___|      | ____|_ __  _   _ _ __ ___  
    | | | |  \| \___ \ _____|  _| | '_ \| | | | '_ ` _ \ 
    | |_| | |\  |___) |_____| |___| | | | |_| | | | | | |
    |____/|_| \_|____/      |_____|_| |_|\__,_|_| |_| |_|
                                                     """ + color.STOP)
    print()
    print ("    "+ "-"*54)
    print()

def banner_osint():
    if sys.platform[:3] == "win":
        command = "cls"
    else:
        command = "clear"
    res = os.system(command)

    print(color.BLUE + """       ___  ____  _   _ ___ _   _ _____ 
     / _ \/ ___|| | | |_ _| \ | |_   _|
    | | | \___ \| |_| || ||  \| | | |  
    | |_| |___) |  _  || || |\  | | |  
     \___/|____/|_| |_|___|_| \_| |_|  """ + color.STOP)

    print()
    print("    "+ "-"*35)
    print()

def main():
    banner()
    while True:
        report = False
        print("    " + "-"*77)
        print(color.BOLD + "0. Banner\n1. Shodan Scans")
        print("2. Web Enumeration")
        print("3. DNS Enumeration")
        print("4. OSINT")
        print("99. Exit")
        print("" + color.STOP)
        choice = int(input(">>> "))
        if choice == 99:
            print(color.BLUE + "[!] GoodBye." + color.STOP)
            sys.exit(0)
        if choice < 0 or choice >= 5:
            print(color.RED + "[-] Unable to process the information, select again." + color.STOP)
            x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
            banner()
            continue
        if choice == 0:
            banner()
            continue
        if choice == 1:
            banner_shodan()
            print(color.BOLD + "\n\n1. API Info \n2. Host Scanner \n3. Search Query\n99. Back to Main Menu" + color.STOP)
            choice1 = int(input(">>> "))
            if choice1 == 99:
                banner()
                continue
            if choice1 < 0 or choice1 > 3:
                print(color.RED + "[-] Unable to process information, select again." + color.STOP)
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice1 == 1:
                rep = input(color.BOLD + "Generate Report? (Y/n): " + color.STOP)
                if rep == 'Y' or rep == 'y':
                    report= True
                api_info.shodan_api_info(report)
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice1 == 2:
                shodan_scan_host.scan_host()
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice1 == 3:
                shodan_search.search()
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
        elif choice == 2:
            banner_web()
            print(color.BOLD + "\n\n1.Web Crawler\n2. DirBuster\n3. Subdomain Lookup\n99.Back to Main Menu" + color.STOP)
            choice2 = int(input(">>> "))
            if choice2 == 99:
                banner()
                continue
            if choice2 < 0 or choice2 > 3:
                print(color.RED + "[-] Unable to process Information, try again later." + color.STOP)
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice2 == 1:
                rep = input(color.BOLD + "Generate Report? (Y/n): " + color.STOP)
                if rep == 'Y' or rep == 'y':
                    report = True
                crawler.scraper(report)
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice2 == 2:
                dirbuster.buster()
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice2 == 3:
                subdomain_lookups.subdomains()
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
        elif choice == 3:
            banner_dns()
            print(color.BOLD + "\n\n1. Check Domain Registration\n2. Whois Information Retrieval\n99. Back to Main Menu" + color.STOP)
            choice3 = int(input(">>> "))
            if choice3 == 99:
                banner()
                continue
            if choice3 < 0 or choice3 > 2:
                print(color.RED + "[-] Unable to process Information, try again later." + color.STOP)
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice3 == 1:
                is_domain_registered.whois_domain()
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice3 == 2:
                whois_info.whois_query()
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
        elif choice == 4:
            banner_osint()
            print(color.BOLD + "\n\n1. Username Recon\n2. Port Scanner\n99. Back to Main Menu." + color.STOP)
            choice4 = int(input(">>> "))
            if choice4 == 99:
                banner()
                continue
            if choice4 < 0 or choice4 > 2:
                print(color.RED + "[-] Unable to process information, try again later." + color.STOP)
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice4 == 1:
                user_recon.user()
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
            if choice4 == 2:
                port_scanner.scanner()
                x = input(color.BLUR + "\nPress Any Key to Continue..."+ color.STOP)
                banner()
                continue
        print("\n")
            

if __name__ == '__main__':
    main()

#banner()