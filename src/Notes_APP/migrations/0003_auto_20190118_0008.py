# Generated by Django 2.1.5 on 2019-01-17 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes_APP', '0002_auto_20190117_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]