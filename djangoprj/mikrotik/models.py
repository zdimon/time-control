from django.db import models

# Create your models here.

class MTUsers(models.Model):
    ip = models.CharField(max_length=250, db_index=True)
    host = models.CharField(max_length=250)
    mac = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)


class MTLogin(models.Model):
    time = models.CharField(max_length=250)
    action = models.CharField(max_length=250)
    ip = models.CharField(max_length=250, db_index=True)
    mac = models.CharField(max_length=250)
    

class MTActivity(models.Model):
    time = models.CharField(max_length=250)
    ip = models.CharField(max_length=250, db_index=True)
    bytes = models.IntegerField(default=0)
    log_records = models.TextField()


class MTSession(models.Model):
    ip = models.CharField(max_length=250, db_index=True)
    host_name = models.CharField(max_length=250)
    log_records = models.TextField()
    mac = models.CharField(max_length=250)

class MTSnapshot(models.Model):
    ip = models.CharField(max_length=250, db_index=True)
    mac = models.CharField(max_length=250, db_index=True)
    time = models.DateTimeField(auto_now_add=True)
    activity = models.IntegerField(default=0)