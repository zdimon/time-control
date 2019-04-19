# Generated by Django 2.2 on 2019-04-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikrotik', '0011_mtusers_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mtactivity',
            name='bytes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mtsnapshot',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]