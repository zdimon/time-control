from django.core.management.base import BaseCommand, CommandError
from djangoprj.settings import API_KEY
import hashlib
import requests
import json
from main.models import WTasks
'''

Getting the list of all account tasks: get_all_tasks
https://your-domain.com/api/admin/?action=get_all_tasks&hash=HASH

Returns the names of active and closed tasks, priority and relative reference to the task 
In this request, the page field is not needed

format 

status": "ok",
    "data": [
    {
            "name": "TITLE",
            "page": "/project/PROJECT_ID/TASK_ID/",
            "status": "done",
            "priority": "0..10",
            "user_from": {
                "email": "USER_EMAIL",
                "name": "USER_NAME"
            },
            "user_to": {
                "email": "USER_EMAIL",
                "name": "USER_NAME"
            },
            "date_added": "YYYY-MM-DD HH:II",
            "date_start": "YYYY-MM-DD",
            "date_end": "YYYY-MM-DD",
            "date_closed": "YYYY-MM-DD HH:II",
            "max_time": "50"
            "max_money": "100"
            "tags": "complete"
            "child": [
                {
                    "name": "SUBTASK_NAME",
                    "page": "/project/PROJECT_ID/TASK_ID/SUBTASK_ID/",
                    "status": "done",
                    "priority": "0..10",
                    "user_from": {
                        "email": "USER_EMAIL",
                        "name": "USER_NAME"
                    },
                    "user_to": {
                        "email": "USER_EMAIL",
                        "name": "USER_NAME"
                    },
                    "date_added": "YYYY-MM-DD HH:II",
                    "date_start": "YYYY-MM-DD",
                    "date_end": "YYYY-MM-DD",
                    "date_closed": "YYYY-MM-DD HH:II"
"max_time": "25"
			"max_money": "50"
			"tags": "complete"
                }
            ]
       }


'''

class Command(BaseCommand):

    def get_tasks(self):
        action = 'get_all_tasks'
        key_str = '%s%s' % (action,API_KEY)
        hash = hashlib.md5(key_str.encode()).hexdigest()
        url = 'https://wezom.worksection.com/api/admin/?action=%s&hash=%s' % (action, hash)
        res = requests.get(url)
        out = json.loads(res.text)
        return out['data']       

    def save_tasks(self, tasks):
        for t in tasks:
            print('Saving %s' % t['name'])
            #print(t)
            #break
            try:
                WTasks.objects.get(page=t['page'])
                print('Task exists!!!')
            except:
                ts = WTasks()
                ts.name = t['name']
                ts.page = t['page']
                ts.status = t['status']
                ts.priority = t['priority']
                ts.user_from = t['user_from']['email']
                ts.user_to = t['user_to']['email']
                ts.date_added = t['date_added']
                #ts.date_start = t['date_start']
                #ts.date_end = t['date_end']
                #ts.date_closed = t['date_closed']
                #ts.max_time = t['max_time']
                #ts.max_money = t['max_money']
                ts.save()

    def handle(self, *args, **options):
        print('Load Tasks')
        tasks = self.get_tasks()
        self.save_tasks(tasks)
