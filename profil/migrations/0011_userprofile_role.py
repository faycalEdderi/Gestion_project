# Generated by Django 2.2.3 on 2019-10-17 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0010_auto_20191016_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('rt', 'RT'), ('liv', 'LIV ')], default=' ', max_length=9),
        ),
    ]
