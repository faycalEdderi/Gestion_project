# Generated by Django 2.2.3 on 2019-11-13 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0023_auto_20191113_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chvalid',
            name='relation',
        ),
    ]
