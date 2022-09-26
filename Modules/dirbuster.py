import requests
import os
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

def buster():
	site = input(color.BOLD + "Domain Name: " + color.STOP)
	report = False
	rep = input(color.BOLD + "Generate Report? (Y/n): " + color.STOP)
	if rep == 'Y' or rep == 'y':
		report = True
	correct_write = list()
	with open("dir_list.txt", 'r') as check_list:
		for line in check_list:
			url = site + "/" + line.strip()
			response = requests.get(url, allow_redirects=False)
			if response.status_code != 404:
				print(color.BLUE + "Found /" + str(line.strip()) + "" + color.STOP)
				correct_write.append(str(url))
		
	'''useragent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
	with open("dir_list.txt", "r") as check_list:
		for line in check_list:
			try:
				site_to_test = "http://" + site + line.replace('\n', "")
				site_request = requests.get(site_to_test, headers=useragent)
				if site_request.status_code == requests.codes.ok:
					correct_write.append(site_to_test + '\n')
					print(color.BLUE + line.replace('\n', "") + " -- Found!" + color.STOP)
				else:
					pass
			except:
				pass
	'''
	if report:
		try:
			url = random_string_generator(12, string.ascii_letters)
			with open("Report/dribuster_" + str(url) + ".txt", 'w') as file:
				for i in correct_write:
					file.write(str(correct_write) + "\n")
			print(color.GREEN + "[+] Report Generated Successfully at Report/dirbuster_" + str(url) + ".txt ." + color.STOP)
		except:
			print(color.RED + "[-] Unable to Generate Report." + color.STOP)

#buster()