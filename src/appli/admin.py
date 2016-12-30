# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Vin, Cepage, Assemblage


class AssemblageInline(admin.TabularInline):
	model = Assemblage
	extra = 1


class VinAdmin(admin.ModelAdmin):
	list_display = ('id','nom', 'millesime', 'couleur', 'cepages', )
	inlines = (AssemblageInline,)
	list_editable = ('nom', 'millesime', 'couleur', 'cepages',)


class CepageAdmin(admin.ModelAdmin):
	list_display = ('id','nom',)
	list_editable = ('nom',)
	#inlines = (AssemblageInline,)


admin.site.register(Vin, VinAdmin)
admin.site.register(Cepage, CepageAdmin)
