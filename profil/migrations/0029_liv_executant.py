# Generated by Django 2.2.3 on 2019-11-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0028_auto_20191113_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='liv',
            name='executant',
            field=models.ManyToManyField(to='profil.ChValid'),
        ),
    ]