import requests
import json

class colors:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def shodan_api_info(report=False):
    shodan_api = open('shodan_api.txt', 'r').readlines()[0]
    url = "https://api.shodan.io/api-info?key=" + shodan_api
    request = requests.get(url)
    txt = request.text
    print(colors.GREEN, end='')
    print("[!] API INFORMATION: ")
    parsed = json.loads(txt)
    print("\tMonitored IPs: ", parsed['monitored_ips'])
    print("\tPlan: ", parsed['plan'])
    print("\tQuery Credits: ", parsed['query_credits'])
    print("\tScan Credits: ", parsed['scan_credits'])
    print("\tUsage Limits:\n", end='')
    print("\t\tMonitored IPs: ", parsed['usage_limits']['monitored_ips'])
    print("\t\tQuery Credits: ", parsed['usage_limits']['query_credits'])
    print("\t\tScan Credits: ", parsed['usage_limits']['scan_credits'] , colors.STOP)
    if report:
        try:
            with open("../Report/api_info.txt", 'w') as file:
                file.write("[!] API INFORMATION: ")
                file.write("\n")
                file.write("\tMonitored IPs: " + str(parsed['monitored_ips']))
                file.write("\n")
                file.write("\tPlan: " + str(parsed['plan']))
                file.write("\n")
                file.write("\tQuery Credits: "+ str(parsed['query_credits']))
                file.write("\n")
                file.write("\tScan Credits: " + str(parsed['scan_credits']))
                file.write("\n")
                file.write("\tUsage Limits:\n")
                file.write("\n")
                file.write("\t\tMonitored IPs: " + str(parsed['usage_limits']['monitored_ips']))
                file.write("\n")
                file.write("\t\tQuery Credits: " + str(parsed['usage_limits']['query_credits']))
                file.write("\n")
                file.write("\t\tScan Credits: " + str(parsed['usage_limits']['scan_credits']))
                file.write("\n")

            print(colors.BLUE+"[+] Report saved successfully at Report folder." + colors.STOP)
        except:
            print(colors.RED + "[-] Unable to create file to save the report." + colors.STOP)


#shodan_api_info(True)
