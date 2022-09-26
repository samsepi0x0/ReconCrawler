import whois
import random
import string

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

def isRegistered(domain_name, report=False):
    try:
        w = whois.whois(domain_name)
        if report:
            try:
                url = random_string_generator(12, string.ascii_letters)
                with open("Report/whois_"+ str(url)+ "_report.txt", 'w') as file:
                    file.write(str(w.domain_name))
                    file.write("\n")
                print(color.GREEN + "[+] Reported Generated Successfully at Report/whois_"+ str(url) + "_report.txt ."+ color.STOP)
            except:
                print(color.RED + "[-] Unable to Create Report." + color.STOP)
    except:
        return False
    else:
        return bool(w.domain_name)

def whois_domain():
    domain_name = input(color.BOLD + "Domain Name: " + color.STOP)
    report = input(color.BOLD + "Generate Report(Y/n): " + color.STOP)
    if report == 'Y' or report == 'y':
        if isRegistered(domain_name, True):
            print(color.GREEN + "[+] Domain is Registered." + color.STOP)
        else:
            print(color.RED + "[-] Domain Name not Registered." + color.STOP)
        return "PASS"
    else:
        if isRegistered(domain_name):
            print(color.GREEN + "[+] Domain is Registered." + color.STOP)
        else:
            print(color.RED + "[-] Domain Name not Registered." + color.STOP)
        return "PASS"

#whois_domain()
