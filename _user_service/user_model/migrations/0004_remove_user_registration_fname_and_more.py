# Generated by Django 4.1.13 on 2024-04-21 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0003_user_registration_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_registration',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='user_registration',
            name='lname',
        ),
    ]
