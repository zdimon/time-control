from django.db import models

# Create your models here.
'''
            "email": "USER_EMAIL",
            "first_name": "USER_FIRST_NAME",
            "last_name": "USER_LAST_NAME",
            "name": "USER_NAME",
            "title": "USER_POSITION",
            "avatar": "URL",
            "company": "USER_COMPANY",
            "department": "USER_DEPARTMENT"

'''


class WUsers(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    email = models.CharField(max_length=250, db_index=True)
    first_name =  models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    avatar = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    department = models.CharField(max_length=250)

'''

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


'''

class WTasks(models.Model):
    name =  models.CharField(max_length=250)
    page = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    priority = models.CharField(max_length=250)
    user_from = models.CharField(max_length=250, db_index=True)
    user_to = models.CharField(max_length=250, db_index=True)
    date_added = models.CharField(max_length=250)
    date_start = models.CharField(max_length=250)
    date_end = models.CharField(max_length=250)
    date_closed = models.CharField(max_length=250)
    max_time = models.CharField(max_length=250)
    max_money = models.CharField(max_length=250)

    def __str__(self):
        return self.name