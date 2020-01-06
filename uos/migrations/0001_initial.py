# Generated by Django 2.2 on 2020-01-06 13:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogueUo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('nbrjouruo', models.CharField(max_length=5)),
                ('prixuo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Etatuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fonction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Niveauuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Perimetre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Plateforme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Statutuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Typeuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Uet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('fonctions', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Fonction')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('perimetretravail', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Perimetre')),
            ],
        ),
        migrations.CreateModel(
            name='Uo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numuo', models.CharField(max_length=20)),
                ('catalogue', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.CatalogueUo')),
                ('etatuo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Etatuo')),
                ('fonction', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Fonction')),
                ('niveauo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Niveauuo')),
                ('plateforme', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Plateforme')),
                ('projet', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Projet')),
                ('statutuo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Statutuo')),
                ('typeuo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Typeuo')),
                ('uet', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Uet')),
            ],
        ),
        migrations.CreateModel(
            name='Pointage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semaine', models.IntegerField()),
                ('point', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5)])),
                ('uo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Uo')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='plateforme',
            name='projets',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Projet'),
        ),
        migrations.AddField(
            model_name='catalogueuo',
            name='niveauuo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Niveauuo'),
        ),
        migrations.AddField(
            model_name='catalogueuo',
            name='typeuo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Typeuo'),
        ),
    ]
