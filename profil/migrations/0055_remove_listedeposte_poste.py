# Generated by Django 2.2.3 on 2020-01-07 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0054_listedeposte_poste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listedeposte',
            name='poste',
        ),
    ]
