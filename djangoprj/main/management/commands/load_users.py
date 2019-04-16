from django.core.management.base import BaseCommand, CommandError
import requests
from djangoprj.settings import API_KEY
import hashlib
import json
'''

1. You can form GET or POST request to the Worksection API using URL http://your-domain.com/api/admin/, where your-domain.com - account address registered in Worksection system. 

The request must contain the following parameters: 
action -name of the action 
page -  the url of the project, tasks or subtasks in the system without the account address. For example: "/project/12345/"
hash - verification record, as MD5 formed from three bonded settings page, action and your apikey .
The account owner can get apikey here:  http://your-domain.com/account/api/  
An example of the formation of the verification records for php language: $hash=md5 ($page.$action.$apikey)

Getting a list of users: get_users
https://your-domain.com/api/admin/?action=get_users&hash=HASH

'''

from main.models import WUsers

def save_users(users):
    for u in users:
        print('Saving %s' % u['name'])
        try:
            WUsers.objects.get(email=u['email'])
            print('User %s exists' % u['email'])
        except:
            nu = WUsers()
            nu.name = u['name']
            nu.email = u['email']
            nu.first_name = u['first_name']
            nu.last_name = u['last_name']
            nu.title = u['title']
            nu.avatar = u['avatar']
            nu.company = u['company']
            nu.department = u['department']
            nu.save()

def get_users():
    action = 'get_users'
    key_str = '%s%s' % (action,API_KEY)
    hash = hashlib.md5(key_str.encode()).hexdigest()
    print('hash = %s' % hash)
    url = 'https://wezom.worksection.com/api/admin/?action=%s&hash=%s' % (action, hash)
    res = requests.get(url)
    out = json.loads(res.text)
    return out['data']
    #for user in out['data']:
    #    print(user['name'])

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Load users key is %s' % API_KEY)
        users = get_users()
        save_users(users)
        #rez = requests.get('https://google.com')
        #print(rez.text)        