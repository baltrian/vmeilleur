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

from djgeojson.serializers import Serializer as GeoJSONSerializer

#from .forms import ContributionForm
from .models import Vin


def consulter(request):

    vins = Vin.objects.all()
    return render(request, 'consulter.html', {
        'vins': vins,
    })


def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( '/consulter' )

    return HttpResponseRedirect('/connexion')