import shodan
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

def scan_host():
    api_key = open("shodan_api.txt").readlines()[0]
    api = shodan.Shodan(api_key)
    hostname = input(color.BOLD + "Host IP Address: " + color.STOP)
    report = input(color.BOLD + "Generate Report (Y/n): " + color.STOP)
    rep = False
    if report == 'Y' or report == 'y':
        rep = True
    detail = api.host(hostname)

    print(color.GREEN + "[+] IP: %s"%(detail['ip_str']))
    print ("[+] Hostnames:\t")
    for i in detail["hostnames"]:
        print (str(i), end='  ')
    print ("\n[+] City:\t%s"%(detail["city"]))
    print ("[+] Organisation:\t%s"%(detail["org"]))
    print ("[+] Operating System:\t%s"%(detail["os"]))
    print ("[+] Ports: ", end='')
    for i in detail['data']:
        print (str(i['port']), end='  ')
    print(color.STOP)
    if rep:
        try:
            url = random_string_generator(12, string.ascii_letters)
            with open("Report/shodan_scan_" + str(url) + "_report.txt", 'w') as file:
                file.write("IP Address: " + str(detail['ip_str']))
                file.write("Hostnames: \t");
                for i in detail["hostnames"]:
                    file.write(str(i) + " ")
                file.write("\n")
                file.write("City: " + str(detail['city']))
                file.write("Organisation: " + str(detail['org']))            
                file.write("Operating System: " + str(detail['os']))
                file.write("Ports:\t")
                for i in detail["data"]:
                    file.write(str(i['port']) + " ")
                file.write("\n")
            print(color.BLUE + "[+] Report Generated Successfully at shodan_scan_" + str(url) + "_report.txt" + color.STOP)
        except:
            print(color.RED + "[-] Unable to generate report. Try again Later." + color.STOP)

    return "PASS"

#scan_host()