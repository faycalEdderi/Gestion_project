# Generated by Django 2.2.3 on 2019-10-15 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='post',
            new_name='poste',
        ),
    ]