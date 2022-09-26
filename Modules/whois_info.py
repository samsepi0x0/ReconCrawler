import whois
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

def whois_query():
    hostname = input(color.BOLD + "WHOIS Domain or Query: " + color.STOP)
    report = False
    rep = input(color.BOLD + "Generate Report? (Y/n): " + color.STOP)
    if rep == 'y' or rep == 'Y':
        report = True
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
    
    if report and isRegistered(hostname):
        try:
            url = random_string_generator(12, string.ascii_letters)
            with open("Report/whois_info_" + str(url) + ".txt", 'w') as file:
                file.write("Registrar Name: " + str(domain.registrar) + "\n")
                file.write("Organisation: " + str(domain.org) + "\n")
                file.write("City: " + str(domain.city) + "\n")
                file.write("State: " + str(domain.state) + "\n")
                file.write("Country: " + str(domain.country) + "\n")
                file.write("ZipCode: " + str(domain.zipcode) + "\n")
                file.write("Name Servers: ")
                file.write("\n")
                for i in domain.name_servers:
                    file.write(str(i) + "\t")
                file.write("\n")
                file.write("Whois Server: " + str(domain.whois_server))
                file.write("\n")
            print(color.BLUE + "[+]Report generated Successfully at Report/whois_info_" + str(url) + ".txt ." + color.STOP) 
        except:
            print(color.RED + "[-]Unable to Generate Report." + color.STOP)
    #print(domain)
    return "PASS"

def isRegistered(domain_name):
    try:
        w = whois.whois(domain_name)
    except:
        return False
    else:
        return bool(w.domain_name)

#whois_query()