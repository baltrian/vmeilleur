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


class Appelation(models.Model):
    nom = models.CharField(max_length=120)

    @property
    def geometry(self):
        geoms = [commune.geometry for commune in self.commune_set.all()]
        geom = MultiPolygon()
        for g in geoms: 
            geom = geom + g
            return geom


class Commune(gis_models.Model):
    insee = models.CharField(max_length=5)
    geometry = gis_models.GeometryCollectionField(blank=True, null=True)
    appelation = models.ForeignKey(Appelation, null=True, blank=True)


class Vin(models.Model):
    nom = models.CharField(max_length=120)
    millesime = models.CharField(max_length=4, blank=True, null=True)
    image = models.ImageField(upload_to="vin/", blank=True, null=True)
    couleur = models.CharField(max_length=7)
    appelation = models.ForeignKey(Appelation, null=True, blank=True)
    cepages = models.ManyToManyField(Cepage, through='Assemblage')

    def __unicode__(self):
        return self.nom

    # Construit une chaîne de caractère représentant l'assemblage
    def get_assemblage(self):
        s = " "
        sC = []
        sP = []
        setCepages = self.cepages.all()
        setAssemblage = Assemblage.objects.filter(vin=self).all()
        for cepage in setCepages :    
            sC.append(cepage.nom)
        for assemblage in setAssemblage :
            sP.append(assemblage.pourcentage)
        for i in range(len(sC)) :
            if (i > 0) :
                s = s + ", "
            s = s + sC[i] + " (" + str(sP[i]) + "%)"
        return s


class Assemblage(models.Model):
    vin = models.ForeignKey(Vin, on_delete=models.CASCADE)
    cepage = models.ForeignKey(Cepage, on_delete=models.CASCADE)
    pourcentage = models.PositiveIntegerField()
