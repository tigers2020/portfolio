# Generated by Django 2.2.6 on 2019-10-26 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
