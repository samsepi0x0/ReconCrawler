import os
import shodan

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def set_key(key):
    filename = "shodan_api.txt"
    try:
        with open(filename, 'w') as writer:
            writer.write(key)
        print(color.GREEN + "[+] Key Saved Successfully." + color.STOP)
        print('\x1b[6;30;42m' + "[?] Testing Key." + color.STOP)
        api = shodan.Shodan(open(filename, 'r').readlines(0)[0])
        try:            
            temp = api.host('8.8.8.8')
            print(color.GREEN + "[+] Valid Key." + color.STOP)
            return "PASS"
        except:
            print(color.RED + "[-] Invalid Key detected." + color.STOP)
    except:
        print(color.RED + "[-] Could not save API in a file." + color.STOP)
