# Generated by Django 2.2.3 on 2020-03-09 08:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uos', '0012_auto_20200309_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uo',
            name='DateDebutUO',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 8, 39, 58, 443128, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='uo',
            name='DateLivraison',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 9, 8, 39, 58, 443152, tzinfo=utc), null=True),
        ),
    ]
