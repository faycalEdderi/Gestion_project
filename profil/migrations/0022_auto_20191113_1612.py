# Generated by Django 2.2 on 2019-11-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0021_auto_20191030_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='poste',
            field=models.CharField(choices=[('ch.MIL', 'CH.MIL'), ('ch.HIL', 'CH.HIL '), ('ch.IS', 'CH.IS '), ('liv', 'LIV'), ('rt', 'RT '), ('pmo', 'PMO'), ('rsop', 'RSOP')], max_length=150),
        ),
    ]
