# Generated by Django 2.2.3 on 2020-03-11 08:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uos', '0012_auto_20200310_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogueuo',
            name='nbr_jour_uo',
            field=models.CharField(error_messages={'max_length': 'Le nombre de jour le ne doit pas depasser 5 chiffres'}, max_length=5),
        ),
        migrations.AlterField(
            model_name='pointage',
            name='semaine',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 11, 8, 37, 51, 117040, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='uo',
            name='date_debut_uo',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 11, 8, 37, 51, 118506, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='uo',
            name='date_livraison',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 11, 8, 37, 51, 118527, tzinfo=utc), null=True),
        ),
    ]
