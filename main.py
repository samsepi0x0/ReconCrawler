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
    
    
    print(color.BLUE +"""
    ██████╗░███████╗░█████╗░░█████╗░███╗░░██╗  ░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗██╗░░░░░███████╗██████╗░
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║  ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██╔══██╗
    ██████╔╝█████╗░░██║░░╚═╝██║░░██║██╔██╗██║  ██║░░╚═╝██████╔╝███████║░╚██╗████╗██╔╝██║░░░░░█████╗░░██████╔╝
    ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║╚████║  ██║░░██╗██╔══██╗██╔══██║░░████╔═████║░██║░░░░░██╔══╝░░██╔══██╗
    ██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚███║  ╚█████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░██║
    ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚══╝  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░╚═╝""" + color.STOP)
    print ("    "+ "-"*104)
    print()

def banner_shodan():
    if sys.platform[:3] == "win":
        command = "cls"
    else:
        command = "clear"
    res = os.system(command)
    print("\n" + color.BLUE + """
    ░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░███╗░░██╗
    ██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗████╗░██║
    ╚█████╗░███████║██║░░██║██║░░██║███████║██╔██╗██║
    ░╚═══██╗██╔══██║██║░░██║██║░░██║██╔══██║██║╚████║
    ██████╔╝██║░░██║╚█████╔╝██████╔╝██║░░██║██║░╚███║
    ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝""" + color.STOP)
    print()
    print ("    "+ "-"*50)
    print()

def banner_web():
    if sys.platform[:3] == "win":
        command = "cls"
    else:
        command = "clear"
    res = os.system(command)
    print(color.BLUE + """
    ░██╗░░░░░░░██╗███████╗██████╗░  ██████╗░███████╗░█████╗░░█████╗░███╗░░██╗
    ░██║░░██╗░░██║██╔════╝██╔══██╗  ██╔══██╗██╔════╝██╔══██╗██╔══██╗████╗░██║
    ░╚██╗████╗██╔╝█████╗░░██████╦╝  ██████╔╝█████╗░░██║░░╚═╝██║░░██║██╔██╗██║
    ░░████╔═████║░██╔══╝░░██╔══██╗  ██╔══██╗██╔══╝░░██║░░██╗██║░░██║██║╚████║
    ░░╚██╔╝░╚██╔╝░███████╗██████╦╝  ██║░░██║███████╗╚█████╔╝╚█████╔╝██║░╚███║
    ░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░  ╚═╝░░╚═╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚══╝""" + color.STOP)
    print()
    print ("    "+ "-"*74)
    print()

def banner_dns():
    if sys.platform[:3] == "win":
        command = "cls"
    else:
        command = "clear"
    res = os.system(command)

    print(color.BLUE + r"""
    ██████╗░███╗░░██╗░██████╗  ███████╗███╗░░██╗██╗░░░██╗███╗░░░███╗
    ██╔══██╗████╗░██║██╔════╝  ██╔════╝████╗░██║██║░░░██║████╗░████║
    ██║░░██║██╔██╗██║╚█████╗░  █████╗░░██╔██╗██║██║░░░██║██╔████╔██║
    ██║░░██║██║╚████║░╚═══██╗  ██╔══╝░░██║╚████║██║░░░██║██║╚██╔╝██║
    ██████╔╝██║░╚███║██████╔╝  ███████╗██║░╚███║╚██████╔╝██║░╚═╝░██║
    ╚═════╝░╚═╝░░╚══╝╚═════╝░  ╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝""" + color.STOP)
    print()
    print ("    "+ "-"*65)
    print()

def banner_osint():
    if sys.platform[:3] == "win":
        command = "cls"
    else:
        command = "clear"
    res = os.system(command)

    print(color.BLUE + """
    ░█████╗░░██████╗██╗███╗░░██╗████████╗
    ██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝
    ██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░
    ██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░
    ╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░
    ░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░""" + color.STOP)

    print()
    print("    "+ "-"*35)
    print()

def main():
    banner()
    while True:
        report = False
        print("    " + "-"*104)
        print(color.BOLD + "\t0. Banner\n\t1. Shodan Scans")
        print("\t2. Web Enumeration")
        print("\t3. DNS Enumeration")
        print("\t4. OSINT")
        print("\t99. Exit")
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
            print(color.BOLD + "\n\n\t1. API Info \n\t2. Host Scanner \n\t3. Search Query\n\t99. Back to Main Menu" + color.STOP)
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
            print(color.BOLD + "\n\n\t1.Web Crawler\n\t2. DirBuster\n\t3. Subdomain Lookup\n\t99.Back to Main Menu" + color.STOP)
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
            print(color.BOLD + "\n\n\t1. Check Domain Registration\n\t2. Whois Information Retrieval\n\t99. Back to Main Menu" + color.STOP)
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
            print(color.BOLD + "\n\n\t1. Username Recon\n\t2. Port Scanner\n\t99. Back to Main Menu." + color.STOP)
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
