# Generated by Django 3.2.2 on 2021-06-01 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0002_userverification_uname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userverification',
            name='user',
        ),
    ]
