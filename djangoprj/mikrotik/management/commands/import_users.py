from django.core.management.base import BaseCommand, CommandError
from mikrotik.models import MTLogin, MTActivity, MTUsers, MTSession
from djangoprj.settings import LOG_DIR, BASE_DIR
import re
import time 
from .utils import analize_log_ip_mac
def import_users():
    print('Importing users')
    for rec in MTSession.objects.all():
        print("Processing .... %s" % rec.ip)
        analize_log_ip_mac(rec.ip,rec.mac,rec.host_name)




class Command(BaseCommand):

    def handle(self, *args, **options):
        start = time.time()
        MTUsers.objects.all().delete()
        import_users()
        end = time.time()
        rez = start-end
        print('Execution time is %s records %s' % (rez,MTUsers.objects.all().count()))

            #for it in rec_arr:
            #    if len(it)>3:
            #        print(it)

        
