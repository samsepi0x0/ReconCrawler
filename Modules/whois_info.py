import whois

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def whois_query():
    hostname = input(color.BOLD + "WHOIS Domain or Query: " + color.STOP)
    if isRegistered(hostname) == False:
        print(color.RED + "[-] Domain is not registered." + color.STOP)
        return None
    
    domain = whois.whois(hostname)
    print(color.GREEN + "[+] Registrar Name: " + color.STOP, domain.registrar)
    print(color.GREEN + "[+] Organisation: " + color.STOP, domain.org)
    print(color.GREEN + "[+] City: " + color.STOP, domain.city)
    print(color.GREEN + "[+] State: " + color.STOP, domain.state)
    print(color.GREEN + "[+] Country: " + color.STOP, domain.country)
    print(color.GREEN + "[+] ZipCode: " + color.STOP, domain.zipcode)
    print(color.GREEN + "[+] Name Servers: " + color.STOP)
    for i in domain.name_servers:
        print("\t", i)
    print(color.GREEN + "[+] Whois Server: " + color.STOP, domain.whois_server)
    
    #print(domain)
    return "PASS"

def isRegistered(domain_name):
    try:
        w = whois.whois(domain_name)
    except:
        return False
    else:
        return bool(w.domain_name)