# Generated by Django 2.2.3 on 2020-03-09 12:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uos', '0022_auto_20200309_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uo',
            name='DateDebutUO',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 12, 3, 31, 8851, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='uo',
            name='DateLivraison',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 12, 3, 31, 8874, tzinfo=utc), null=True),
        ),
    ]
