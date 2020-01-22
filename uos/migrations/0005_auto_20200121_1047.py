# Generated by Django 2.2 on 2020-01-21 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uos', '0004_auto_20200120_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uo',
            old_name='jalaonD',
            new_name='jalonD',
        ),
        migrations.RenameField(
            model_name='uo',
            old_name='jalaonF',
            new_name='jalonF',
        ),
        migrations.AddField(
            model_name='uo',
            name='Client',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='uo',
            name='avancement',
            field=models.FloatField(default=0),
        ),
    ]