# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-29 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assemblage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pourcentage', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Vin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=120)),
                ('millesime', models.CharField(blank=True, max_length=4, null=True)),
                ('couleur', models.CharField(max_length=7)),
                ('cepages', models.ManyToManyField(through='appli.Assemblage', to='appli.Cepage')),
            ],
        ),
        migrations.AddField(
            model_name='assemblage',
            name='cepage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli.Cepage'),
        ),
        migrations.AddField(
            model_name='assemblage',
            name='vin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appli.Vin'),
        ),
    ]
