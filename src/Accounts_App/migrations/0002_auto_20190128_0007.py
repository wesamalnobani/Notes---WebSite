# Generated by Django 2.1.5 on 2019-01-27 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
