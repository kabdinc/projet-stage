# Generated by Django 4.0.6 on 2022-07-21 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20220721_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervenant',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
