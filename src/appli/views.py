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

from djgeojson.serializers import Serializer as GeoJSONSerializer

#from .forms import ContributionForm
from .models import Vin


def consulter(request):

    vins = Vin.objects.all()
    return render(request, 'consulter.html', {
        'vins': vins,
    })
