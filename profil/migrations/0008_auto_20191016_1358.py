# Generated by Django 2.2.3 on 2019-10-16 11:58

from django.db import migrations, models
import profil.models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0007_auto_20191016_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profil.models.upload_location),
        ),
    ]