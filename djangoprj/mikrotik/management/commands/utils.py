from mikrotik.models import MTActivity, MTLogin, MTSession, MTUsers
from djangoprj.settings import LOG_DIR, BASE_DIR
import re
import time
import sys

def analize_log_ip_mac(ip,mac,host_name):
    try:
        MTUsers.objects.get(mac=mac)
        print("User with mac - %s exists" % mac)
    except:
        user = MTUsers()
        user.ip = ip
        user.mac = mac
        user.host = host_name
        user.save()
        print("Creatimg user %s" % mac)


def import_session():
    MTSession.objects.all().delete()    
    lpath = '%s/%s' % (BASE_DIR,LOG_DIR)
    fname = '%s/dhcp-sessions.log' % lpath
    print('Load Logs from %s' % fname)
    # open and read file
    f = open(fname,'r')
    txt = f.read()
    f.close()
    log_array = txt.split('\n\n')
    #print(log_array)
    for rec in log_array:
        #print("Importing users sessions")
        try:
            match = re.search('host-name="(.*)"',rec)
            hname = match.group(1)
            print('HOST NAME = %s' % hname)
        except:
            hname = 'undefined'
            #print(rec)
            #sys.exit('Error geting mac adress')
    
        try:
            match = re.search('address=(.*) mac-address',rec)
            ip = match.group(1)
            print('ip = %s' % ip)
        except:
            pass

        try:
            match = re.search('mac-address=(.*) address-lists',rec)
            mac = match.group(1)
            print('mac = %s' % mac)
        except:
            try:
                match = re.search('active-mac-address=(.*)\n',rec)
                mac = match.group(1)
            except:
                try:
                    match = re.search('src-mac-address=(.*)',rec)
                    mac = match.group(1)
                except:
                    #print(rec)
                    #sys.exit('Error geting mac adress')
                    mac = 'empty'

        slog = MTSession()
        slog.ip = ip
        slog.host_name = hname
        slog.mac = mac
        slog.log_records = rec
        slog.save()
        '''
        try:
            user = MTUsers.objects.get(ip=ip)
        except:
            user = MTUsers()

        user.ip = ip
        user.mac = mac
        user.host_name = hname
        user.save()           
        ''' 


def import_login():
    MTLogin.objects.all().delete()    
    lpath = '%s/%s' % (BASE_DIR,LOG_DIR)
    fname = '%s/dhcp-login.log' % lpath
    print('Load Logs from %s' % fname)
    # open and read file
    f = open(fname,'r')
    txt = f.read()
    f.close()
    log_array = txt.split('\n\n')
    print(log_array)
    for rec in log_array:
        rec_arr = rec.split(' ')
        print('-----------------------')
        #print(rec)

        try:
            match = re.search('time=(.*)topics',rec)
            tm = match.group(1)
            print('Time = %s' % tm)
        except:
            #print('ERROR')
            #print(rec)
            continue

        try:
            match = re.search('from \n(.*)"',rec)
            mac = match.group(1)
        except:
            match = re.search('to \n(.*)"',rec)
            mac = match.group(1)                
        print('MAC adress = %s' % mac)

        try:
            match = re.search('assigned (.*) to',rec)
            ip = match.group(1)            
        except:
            match = re.search('deassigned (.*) from',rec)
            ip = match.group(1)                 

        print('IP adress = %s' % ip)

        log = MTLogin()
        log.ip = ip
        log.time = tm
        log.mac = mac
        log.save()    



def import_activity_log():
    MTActivity.objects.all().delete()
    lpath = '%s/%s' % (BASE_DIR,LOG_DIR)
    fname = '%s/activity.log' % lpath
    print('Load Logs from %s' % fname)
    # open and read file
    f = open(fname,'r')
    txt = f.read()
    f.close()
    log_array = txt.split('\n\n')
    #print(log_array)
    for rec in log_array[1:len(log_array)]:

        rec_arr = rec.split(' ')
        print('-----------------------')
        #print(rec)

        try:
            match = re.search(' src-address=(.*):[0-9]',rec)
            ip = match.group(1)
            #ip = re.search('\b(?:\d{1,3}\.){3}\d{1,3}\b',ip)
            #ip = match.group(1)
            #if len(ip)> 20:
            #    import pdb; pdb.set_trace()
            ip = ip.split(':')[0]
            print('IP = %s' % ip)
        except Exception as e:
            continue   

        try:
            match = re.search('timeout=(.*) orig-packets',rec)
            timout = match.group(1)
            print('TIMEOUT = %s' % timout)
        except:
            timout = '0'
             
        try:
            match = re.search('repl-packets=(.*)\n(.*)repl-bytes',rec)
            activity = match.group(1)
            print('Activity = %s' % activity)
        except:
            activity = '0'           

        
                

        log = MTActivity()
        log.ip = ip
        log.time = timout
        log.bytes = int(activity.replace(' ',''))
        log.log_records = rec
        log.save()
    return True  