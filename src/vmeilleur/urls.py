# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin

from appli.views import consulter


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #url(r'^$', contribuer, name="contribuer"),
    #url(r'^$', name="contribuer"),
    #url(r'^resultat/(?P<pk>\d+)/$', resultat, name="resultat"),
    url(r'^consulter/', consulter, name="consulter"),

    #url(r'^contribuer_json/$', contribuer, name="contribuer_json"),
]

admin.site.site_header = "Le meilleur"
