# Generated by Django 4.0.6 on 2023-04-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maquette', '0004_anneeacademique_classe_anneeacademique_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matiere',
            name='coefficient',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='unitenseignement',
            name='credit',
            field=models.SmallIntegerField(null=True),
        ),
    ]
