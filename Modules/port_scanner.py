import sys
import os
import socket


class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def scanner():
    print(color.BOLD + "1. Domain Name \n2. IP Address" + color.STOP)
    ch = int(input(">>> "))
    if ch < 1 or ch > 2:
        print(color.RED + "[-] Invalid Choice" + color.STOP)
        return None
    if ch == 1:
        domain = input(color.BOLD + "  Domain Name: " + color.STOP)
        try:
            ip_addr = socket.gethostbyname(domain)
        except:
            print(color.RED + "[-] Could not resolve Domain" + color.STOP)
            return None
    else:
        ip_addr = input(color.BOLD + "  IP Address: " + color.STOP)
    
    port_start = int(input(color.BOLD + "\nPort range(Start): " + color.STOP))
    port_end = int(input(color.BOLD + "Port range(End): " + color.STOP))

    if port_start > port_end:
        print(color.RED + "[-] Unable to perform Scan on said range." + color.STOP)
        return None

    for i in range(port_start, port_end):
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if con.connect_ex((ip_addr, i)) == 0:
            print('\x1b[6;30;42m' + "[+] Found Open Port on : {}".format(i) + color.STOP)
        con.close()

    print()
    return "PASS"
