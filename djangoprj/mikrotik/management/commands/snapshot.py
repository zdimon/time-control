from django.core.management.base import BaseCommand, CommandError
from mikrotik.models import MTLogin, MTActivity, MTUsers, MTSnapshot
import re
import time 
from django.db.models import Sum
from .utils import import_activity_log, import_login, import_session
import sys

class Command(BaseCommand):

    def handle(self, *args, **options):
        start = time.time()
        print("Taking snapshot")
        ok = 0
        fail = 0
        for user in MTUsers.objects.all():
            #print("Process --- %s" % user.mac)
            try:
                act = MTActivity.objects.filter(ip=user.ip).aggregate(total=Sum('bytes'))
                print(act)
                if act['total'] == None:
                    #print(MTActivity.objects.filter(ip=user.ip).query)
                    act['total'] = 0
                    #sys.exit('stop')
                ok +=1
                s = MTSnapshot()
                s.ip = user.ip
                s.mac = user.mac.strip()
                s.activity = act['total']
                s.save()


            except Exception as e:
                print("Can NOT find!")
                print(str(e))
                fail += 1
        end = time.time()
        rez = start-end
        print("Execution time = %s OK-%s FAIL-%s" % (rez,ok,fail))
        
        
