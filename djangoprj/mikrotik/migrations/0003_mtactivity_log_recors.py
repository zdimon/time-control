# Generated by Django 2.2 on 2019-04-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mikrotik', '0002_mtactivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtactivity',
            name='log_recors',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
