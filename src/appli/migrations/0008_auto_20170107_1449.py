# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-07 14:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0007_auto_20170107_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commune',
            name='appelation',
        ),
        migrations.AddField(
            model_name='commune',
            name='appelations',
            field=models.ManyToManyField(blank=True, null=True, to='appli.Appelation'),
        ),
    ]
