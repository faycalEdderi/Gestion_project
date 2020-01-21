# Generated by Django 2.2.3 on 2020-01-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0047_auto_20191202_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='poste',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('pmo', 'PMO'), ('rsop', 'RSOP'), ('rt', 'RT'), ('pilote_activite', "PILOTE D'ACTIVITÉ"), ('charge_execution', 'CH.EXECUTION')], default='charge_execution', max_length=20),
        ),
    ]