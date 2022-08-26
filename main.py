import sys
import os
from Modules import is_domain_registered
from Modules import whois_info
from Modules import subdomain_lookups
from Modules import crawler
#from Modules import dirbuster
from Modules import port_scanner
from Modules import shodan_set_key
from Modules import shodan_scan_host
from Modules import shodan_search
from Modules import user_recon

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

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

def main():
    banner()
    while True:
        print("    " + "-"*77)
        print(color.BOLD+"0. Banner")
        print("1. Whois Domain Registery")
        print("2. Whois Information")
        print("3. Subdomain Lookup")
        print("4. Web Crawler")
        print("5. Web Directory Bruteforcing")
        print("6. Port Scanner")
        print("7. Shodan Set API Key")
        print("8. Shodan Scan IP Address")
        print("9. Shodan Search Query")
        print("10.Username recon")
        print("99.Exit")
        print("" + color.STOP)
        choice = int(input(">>> "))
        if choice == 99:
            print(color.BLUE + "[!] GoodBye." + color.STOP)
            sys.exit(0)
        if choice < 0 or choice > 10:
            print(color.RED + "[-] Unable to process the information, selection again." + color.STOP)
            banner()
            continue
        if choice == 0:
            banner()
        if choice == 1:
            status = is_domain_registered.whois_domain()
        elif choice == 2:
            status = whois_info.whois_query()
        elif choice == 3:
            status = subdomain_lookups.subdomains()
        elif choice == 4:
            status = crawler.scraper()
        elif choice == 5: 
            print('\x1b[6;30;42m' + "[?] To be Fixed." + color.STOP)
        elif choice == 6: 
            status = port_scanner.scanner()
        elif choice == 7: 
            key = input(color.BOLD + "Shodan API key: " + color.STOP)
            status = shodan_set_key.set_key (key)
        elif choice == 8: 
            status = shodan_scan_host.scan_host()
        elif choice == 9: 
            status = shodan_search.search()
        elif choice == 10: 
            user_recon.user()
        print("\n")
            

if __name__ == '__main__':
    main()

banner()