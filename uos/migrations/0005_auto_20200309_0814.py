# Generated by Django 2.2.3 on 2020-03-09 07:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uos', '0004_auto_20200309_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uo',
            name='DateDebutUO',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 7, 14, 49, 977759, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='uo',
            name='DateLivraison',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 7, 14, 49, 977784, tzinfo=utc), null=True),
        ),
    ]
