# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-01 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appli', '0002_auto_20161230_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='vin',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vin/'),
        ),
    ]