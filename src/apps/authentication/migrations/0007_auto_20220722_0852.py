# Generated by Django 3.1.7 on 2022-07-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_intervenant_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='intervenant',
            name='Type',
        ),
        migrations.AlterField(
            model_name='intervenant',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='intervenant',
            name='Type',
            field=models.ManyToManyField(to='authentication.Type'),
        ),
    ]
