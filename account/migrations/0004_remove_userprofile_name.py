# Generated by Django 4.2.6 on 2024-03-25 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_userprofile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='name',
        ),
    ]
