import shodan

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
    return "PASS"
