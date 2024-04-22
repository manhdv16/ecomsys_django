# Generated by Django 4.1.13 on 2024-04-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.FileField(blank=True, null=True, upload_to='clothes/images')),
                ('brand', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100, null=True)),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Unisex', 'Unisex')], max_length=50)),
            ],
            options={
                'db_table': 'clothes',
            },
        ),
    ]