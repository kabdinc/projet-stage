# Generated by Django 4.0.6 on 2022-07-21 14:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_intervenant_options_alter_intervenant_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervenant',
            name='Type',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
