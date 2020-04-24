# Generated by Django 2.2.4 on 2020-04-01 13:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointage',
            name='semaine',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 1, 13, 34, 36, 822644, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='uo',
            name='date_debut_uo',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 1, 13, 34, 36, 824638, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='uo',
            name='date_livraison',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 1, 13, 34, 36, 824638, tzinfo=utc), null=True),
        ),
    ]