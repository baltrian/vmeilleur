# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Vin, Cepage, Assemblage, Appelation, Commune


class AssemblageInline(admin.TabularInline):
	model = Assemblage
	extra = 1


class VinAdmin(admin.ModelAdmin):
	list_display = ('id','nom', 'millesime', 'couleur', 'appelation','image',)
	inlines = (AssemblageInline,)
	list_editable = ('nom', 'millesime', 'couleur', 'appelation','image',)


class CepageAdmin(admin.ModelAdmin):
	list_display = ('id','nom',)
	list_editable = ('nom',)
	#inlines = (AssemblageInline,)

class AppelationAdmin(admin.ModelAdmin):
    list_display = ('id','nom',)
    list_editable = ('nom',)
    #inlines = (AssemblageInline,)


class CommuneAdmin(admin.ModelAdmin):
    list_display = ('id', 'insee')
    list_editable = ('insee',)

admin.site.register(Vin, VinAdmin)
admin.site.register(Cepage, CepageAdmin)
admin.site.register(Appelation, AppelationAdmin)
admin.site.register(Commune, CommuneAdmin)
