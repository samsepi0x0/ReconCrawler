import requests
import os

def buster():
    """
        Work in progress.
    """
    try:
		url = input("URL(https://...): ")
		r=requests.get(url)
		if r.status_code == 200:
			print("[+] Host is up.")
		else:
			print("[-] Host is down.")
			return None
        wordlist = input("Wordlist: ")
		if os.path.exists(os.getcwd()+wordlist):
			fs=open(os.getcwd()+wordlist,"r")
			for i in fs:
				print(url+"/"+i)
				rq=requests.get(url+"/"+i)
				if rq.status_code == 200:
					print("[+] OK".rjust(len(url+"/"+i)+5,'-'))
					arr.append(str(url+"/"+i))
				else:
					print("[+] 404".rjust(len(url+"/"+i)+5,'-'))
			fs.close()
			print("output".center(100,'-'))
			l=1
			for i in arr:
				print(l, "> ", i)
				l+=1
        return "PASS"
		else:
			print("[-] " + wordlist +" does not exists in the Module Directory.")
            return None
	except Exception as e:
		print("[-] Exception Occured. Try Again Later.")
        return None
