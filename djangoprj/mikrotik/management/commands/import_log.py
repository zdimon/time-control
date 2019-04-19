from django.core.management.base import BaseCommand, CommandError
from mikrotik.models import MTLogin, MTActivity
import re
import time 

from .utils import import_activity_log, import_login, import_session


class Command(BaseCommand):

    def handle(self, *args, **options):
        start = time.time()
        import_activity_log()
        import_login()
        import_session()
        end = time.time()
        rez = start-end
        print('Execution time is %s records %s' % (rez,MTLogin.objects.all().count()))

        
