# Generated by Django 4.0.2 on 2022-02-14 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Meetups',
            new_name='Meetup',
        ),
    ]
