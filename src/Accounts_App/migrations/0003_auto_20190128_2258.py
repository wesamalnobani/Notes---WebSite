# Generated by Django 2.1.5 on 2019-01-28 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts_App', '0002_auto_20190128_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
