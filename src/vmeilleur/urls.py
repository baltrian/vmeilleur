# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from appli.views import consulter, login#, informationVin


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    # On import les vues de Django, avec un nom spécifique
	url(r'^login', auth_views.login, {'template_name': 'login.html'}),	

    #url(r'^$', contribuer, name="contribuer"),
    #url(r'^$', name="contribuer"),
    #url(r'^resultat/(?P<pk>\d+)/$', resultat, name="resultat"),
    url(r'^consulter[//]*', consulter, name="consulter"),
    #url(r'^informationVin[//]*', informationVin, name="informationVin"),

    url(r'^[A-Za-z0-9-//]*$', auth_views.login, {'template_name': 'connexion.html'}),

    #url(r'^contribuer_json/$', contribuer, name="contribuer_json"),
]

admin.site.site_header = "Le meilleur"
