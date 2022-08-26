import whois

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def isRegistered(domain_name):
    try:
        w = whois.whois(domain_name)
    except:
        return False
    else:
        return bool(w.domain_name)

def whois_domain():
    domain_name = input(color.BOLD + "Domain Name: " + color.STOP)
    if isRegistered(domain_name):
        print(color.GREEN + "[+] Domain is Registered." + color.STOP)
    else:
        print(color.RED + "[-] Domain Name not Registered." + color.STOP)
    return "PASS"

