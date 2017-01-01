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
from .models import Vin

@login_required
def consulter(request):

    vins = Vin.objects.all()
    return render(request, 'consulter.html', {
        'vins': vins,
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


#def informationVin(reques):
 ###   vin = Vin.get();
  ###      return render(request, 'informationVin.html', {
  ##      'vin': vin,
  #  })