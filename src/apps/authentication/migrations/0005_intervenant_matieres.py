# Generated by Django 4.0.6 on 2023-06-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maquette', '0013_alter_classe_niveau_classe'),
        ('authentication', '0004_remove_intervenant_classes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervenant',
            name='matieres',
            field=models.ManyToManyField(to='maquette.matiere'),
        ),
    ]
