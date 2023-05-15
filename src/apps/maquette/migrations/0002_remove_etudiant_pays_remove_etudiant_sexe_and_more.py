# Generated by Django 4.0.6 on 2023-04-14 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maquette', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='pays',
        ),
        migrations.RemoveField(
            model_name='etudiant',
            name='sexe',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='cycle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='maquette.cycle'),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='date_naissance',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='filiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='maquette.filiere'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='nom',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='prenoms',
            field=models.CharField(max_length=50),
        ),
    ]
