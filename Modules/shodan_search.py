import shodan
import json
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

def search():
    try:
        api_key = open("shodan_api.txt", 'r').readlines()[0]
        api = shodan.Shodan(api_key)
        query = input(color.BOLD + "Search Query: " + color.STOP)
        report = False
        rep = input(color.BOLD + "Generate Report? (Y/n): " + color.STOP)
        if rep == 'Y' or rep == 'y':
            report = True
        result = api.search(query)
        if result['matches'][0]['ip'] is not None:
            print('\x1b[6;30;42m' + "[?] Found Matches: " + color.STOP)
            for res in result['matches']:
                print(color.GREEN + "[+] IP: " + color.STOP, res['ip_str'], end='')
                print(" "*(12-len(res['ip_str'])), end='')
                print(color.GREEN + "\tPORT: " + color.STOP, res['port'], color.GREEN + "\tORG: " + color.STOP, res['org'], color.STOP)
        if report:
            try:
                url = random_string_generator(12, string.ascii_letters)
                with open("Report/shodan_search_" + str(url) + ".txt", 'w') as file:
                    file.write("Matches: \n")
                    if result['matches'][0]['ip'] is not None:
                        for res in result['matches']:
                            file.write("IP: " + str(res['ip_str']) + "\tPort: " + str(res['port']) + "\tORG: " + str(res['org']) + "\n")
                    print(color.GREEN + "[+] Report Generated successfully at Report/shodan_search_" + str(url) + ".txt ." + color.STOP)
            except:
                print(color.RED + "[-] Unable to Generate Report." + color.STOP)    
        return "PASS"
    except:
        print(color.RED + "[-] Exception Occured. Try again later." + color.STOP)
        return None

#search()