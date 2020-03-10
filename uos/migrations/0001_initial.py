# Generated by Django 2.2.3 on 2020-03-10 08:37

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donnees_dentree', models.CharField(default='', max_length=600)),
                ('activite_attendue', models.CharField(default='', max_length=600)),
                ('pourcentage_dactivite', models.FloatField()),
                ('conditions_de_reussite', models.CharField(default='', max_length=600)),
                ('date_donnees_dentrees', models.DateTimeField(blank=True, default='')),
                ('date_de_demarrage_dactivite', models.DateTimeField(blank=True, default='')),
                ('livrable_attendu', models.CharField(default='', max_length=600)),
                ('date_reception_attendu_du_Livrable', models.DateTimeField(blank=True, default='')),
                ('commentaires_sur_attendu', models.CharField(default='', max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='CatalogueUo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('nbr_jour_uo', models.CharField(max_length=5)),
                ('prix_uo', models.CharField(max_length=20)),
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
            name='Lot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
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
            name='NotedeCadrage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('reponseRSA', models.CharField(blank=True, default='', max_length=600, null=True)),
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
            name='Pointage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semaine', models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 10, 8, 37, 5, 484326, tzinfo=utc), null=True)),
                ('point_pilote', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5)])),
                ('point_exceutant', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5)])),
                ('excutant', models.ManyToManyField(default='', to='profil.Executant')),
                ('pilote', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='profil.Pilote')),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('plateforme', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Plateforme')),
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
            ],
        ),
        migrations.CreateModel(
            name='WorkPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Uo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_uo', models.CharField(max_length=20)),
                ('jalon_d', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('jalon_f', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('ju', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('date_debut_uo', models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 10, 8, 37, 5, 485995, tzinfo=utc), null=True)),
                ('date_livraison', models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 10, 8, 37, 5, 486020, tzinfo=utc), null=True)),
                ('avancement', models.FloatField(blank=True, default=0, null=True)),
                ('catalogue', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.CatalogueUo')),
                ('client', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.Client')),
                ('etat_uo', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.Etatuo')),
                ('fonction', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.Fonction')),
                ('lot', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Lot')),
                ('nivea_uo', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.Niveauuo')),
                ('note_de_cadrage', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.NotedeCadrage')),
                ('pilote_activitees', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.Pilote')),
                ('plateforme', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.Plateforme')),
                ('pointage', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.Pointage')),
                ('projet', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.Projet')),
                ('statut_uo', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.Statutuo')),
                ('type_uo', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.Typeuo')),
                ('uet', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='uos.Uet')),
            ],
        ),
        migrations.CreateModel(
            name='Perimetre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('workPackage', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.WorkPackage')),
            ],
        ),
        migrations.CreateModel(
            name='Livraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jalon', models.CharField(default='', max_length=60)),
                ('pourcentage_livre', models.FloatField()),
                ('commentaire', models.CharField(default='', max_length=600)),
                ('niveau_uo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Niveauuo')),
                ('nom_livrable', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Activites')),
                ('numero_uo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Uo')),
                ('projet', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Projet')),
                ('systeme_adas', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Fonction')),
                ('type_uo', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Typeuo')),
            ],
        ),
        migrations.AddField(
            model_name='fonction',
            name='uet',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Uet'),
        ),
        migrations.AddField(
            model_name='catalogueuo',
            name='niveau',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Niveauuo'),
        ),
        migrations.AddField(
            model_name='catalogueuo',
            name='perimetre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Perimetre'),
        ),
        migrations.AddField(
            model_name='catalogueuo',
            name='typeuo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.Typeuo'),
        ),
        migrations.AddField(
            model_name='activites',
            name='note_de_cadrage',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='uos.NotedeCadrage'),
        ),
    ]
