# Generated by Django 2.2 on 2019-04-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('avatar', models.CharField(max_length=250)),
                ('company', models.CharField(max_length=250)),
                ('department', models.CharField(max_length=250)),
            ],
        ),
    ]
