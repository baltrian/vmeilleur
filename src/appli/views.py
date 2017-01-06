# -*- coding: utf-8 -*-
from collections import Counter
from datetime import datetime
import json
import requests
import subprocess
import xml.etree.ElementTree

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.sites.models import Site
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from djgeojson.serializers import Serializer as GeoJSONSerializer

#from .forms import ContributionForm
from .models import Vin, Commune, Appelation

@login_required
def consulter(request):
    geojson = GeoJSONSerializer().serialize(Appelation.objects.all(),
          geometry_field='geometry',
          properties=('nom', 'geometry'))
    vins = Vin.objects.all()
    return render(request, 'consulter.html', {
        'vins': vins,
        'geojson': geojson,
    })


def login(request):

    return render(request, 'login.html', {})


def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( '/consulter' )

    return HttpResponseRedirect('/connexion')


def informationVin(request, id):
    vin = Vin.objects.get(id=id)
    assemblage = vin.get_assemblage()
    geojson = GeoJSONSerializer().serialize(Appelation.objects.all(),
        geometry_field='geometry',
        properties=('nom', 'geometry'))
    return render(request, 'informationVin.html', {
        'vin': vin,
        'assemblage': assemblage,
        'geojson': geojson,
         })