import shodan
import json

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def search():
    try:
        api_key = open("shodan_api.txt", 'r').readlines()[0]
        api = shodan.Shodan(api_key)
        query = input(color.BOLD + "Search Query: " + color.STOP)
        result = api.search(query)
        if result['matches'][0]['ip'] is not None:
            print('\x1b[6;30;42m' + "[?] Found Matches: " + color.STOP)
            for res in result['matches']:
                print(color.GREEN + "[+] IP: " + color.STOP, res['ip_str'], end='')
                print(" "*(12-len(res['ip_str'])), end='')
                print(color.GREEN + "\tPORT: " + color.STOP, res['port'], color.GREEN + "\tORG: " + color.STOP, res['org'] + color.STOP)
        return "PASS"
    except:
        print(color.RED + "[-] Exception Occured. Try again later." + color.STOP)
        return None
