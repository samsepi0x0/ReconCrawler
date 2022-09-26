import sys
import os
import socket
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

def scanner():
    print(color.BOLD + "1. Domain Name \n2. IP Address" + color.STOP)
    ch = int(input(">>> "))
    rep = False
    report = input(color.BOLD + "Generate Report (Y/n): " + color.STOP)
    if report == 'Y' or report == 'y':
        rep = True
    else:
        rep = False

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
    ports = list()
    for i in range(port_start, port_end):
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if con.connect_ex((ip_addr, i)) == 0:
            print('\x1b[6;30;42m' + "[+] Found Open Port on : {}".format(i) + color.STOP)
            ports.append(i)
        con.close()

    if rep:
        url = random_string_generator(12, string.ascii_letters)
        try:
            with open("Report/port_scanner_" + url + ".txt", 'w') as file:
                file.write("Found Opean ports on IP: " + str(ip_addr) + "\n")
                for i in ports:
                    file.write(str(i))
                    file.write("\n")
            print(color.BLUE + "[+]Report Generated Successfully at port_scanner_" + str(url) + ".txt ." + color.STOP)
        except:
            print(color.RED + "[-] Unable to generate Report. Try Again Later." + color.STOP)
    print()
    return "PASS"

#scanner()