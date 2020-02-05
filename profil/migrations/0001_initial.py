# Generated by Django 2.2.3 on 2020-01-22 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profil.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChValid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NewPostName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(error_messages={'unique': 'Ce poste existe déja !'}, max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=profil.models.upload_location)),
                ('role', models.CharField(choices=[('pmo', 'PMO'), ('rsop', 'RSOP'), ('rt', 'RT'), ('pilote_activite', "PILOTE D'ACTIVITÉ"), ('charge_execution', 'CH.EXECUTION')], default='charge_execution', max_length=20)),
                ('is_active', models.CharField(blank=True, choices=[('activate', 'actif'), ('desactivate', 'desactive ')], default='activate', max_length=15, null=True)),
                ('poste', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='profil.NewPostName')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Liv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executant', models.ManyToManyField(blank=True, related_name='liv', to='profil.ChValid')),
                ('rt_liv', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.Rt')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='chvalid',
            name='responsable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.Liv'),
        ),
        migrations.AddField(
            model_name='chvalid',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
