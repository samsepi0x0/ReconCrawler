import requests
import json

class color:
    GREEN = '\033[92m'
    STOP = '\033[0m'
    RED='\033[31m'
    BLUE='\033[94m'
    BOLD = '\033[93m'

def shodan_api_info():
    shodan_api = open('shodan_api.txt', 'r').readlines()[0]
    url = "https://api.shodan.io/api-info?key=" + shodan_api
    request = requests.get(url)
    txt = request.text
    print(color.GREEN, end='')
    print("[!] API INFORMATION: ")
    parsed = json.loads(txt)
    print("\tMonitored IPs: ", parsed['monitored_ips'])
    print("\tPlan: ", parsed['plan'])
    print("\tQuery Credits: ", parsed['query_credits'])
    print("\tScan Credits: ", parsed['scan_credits'])
    print("\tUsage Limits:\n", end='')
    print("\t\tMonitored IPs: ", parsed['usage_limits']['monitored_ips'])
    print("\t\tQuery Credits: ", parsed['usage_limits']['query_credits'])
    print("\t\tScan Credits: ", parsed['usage_limits']['scan_credits'] + colors.STOP)