# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from collections import defaultdict, Counter

from django.db import models
from django.db.models import Count
from django.contrib.gis.db import models as gis_models
from django.utils.text import slugify


class Cepage(models.Model):
    nom = models.CharField(max_length=120)

    def __unicode__(self):
        return self.nom


class Vin(models.Model):
    nom = models.CharField(max_length=120)
    millesime = models.CharField(max_length=4, blank=True, null=True)
    #image = models.ImageField(upload_to="waste/", blank=True, null=True)
    couleur = models.CharField(max_length=7)
    cepages = models.ManyToManyField(Cepage, through='Assemblage')

    def __unicode__(self):
        return self.nom


class Assemblage(models.Model):
    vin = models.ForeignKey(Vin, on_delete=models.CASCADE)
    cepage = models.ForeignKey(Cepage, on_delete=models.CASCADE)
    pourcentage = models.PositiveIntegerField()
