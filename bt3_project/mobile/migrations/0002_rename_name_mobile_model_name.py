# Generated by Django 4.1.13 on 2024-03-14 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mobile',
            old_name='name',
            new_name='model_name',
        ),
    ]
