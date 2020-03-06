# Generated by Django 2.2 on 2020-03-06 07:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uos', '0003_auto_20200306_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uo',
            name='Client',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='uo',
            name='DateDebutUO',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 6, 7, 43, 11, 78817, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uo',
            name='DateLivraison',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 6, 7, 43, 11, 78817, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uo',
            name='avancement',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='uo',
            name='catalogue',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.CatalogueUo'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='etatuo',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Etatuo'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='fonction',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Fonction'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='jalonD',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='uo',
            name='jalonF',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='uo',
            name='ju',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='uo',
            name='lot',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Lot'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='niveauo',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Niveauuo'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='notedeCadrage',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.NotedeCadrage'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='piloteUo',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='uo',
            name='plateforme',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Plateforme'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='pointage',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Pointage'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='projet',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Projet'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='statutuo',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Statutuo'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='typeuo',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Typeuo'),
        ),
        migrations.AlterField(
            model_name='uo',
            name='uet',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Uet'),
        ),
    ]
