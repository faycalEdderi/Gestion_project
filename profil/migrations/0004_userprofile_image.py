# Generated by Django 2.2.3 on 2019-10-16 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0003_auto_20191015_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]
