from django.contrib import admin
from klienti.models import *


class KlientiAdmin(admin.ModelAdmin):
    list_display = ['vards', 'e_pasts', 'tel','pirmais_pieteikums', 'pedejais_pieteikums', 'pieteikuma_reizes', 'atteikuma_reizes']
    list_filter = ['pirmais_pieteikums', 'pedejais_pieteikums']
    search_fields = ['vards', 'e_pasts', 'tel']
    exclude = ['pirmais_pieteikums', 'pedejais_pieteikums', 'atteikuma_reizes', 'pieteikuma_reizes']


class HistPierakstiAdmin(admin.ModelAdmin):
    list_display = ['pieraksta_laiks', 'klients', 'nodarbiba']


admin.site.register(Klienti, KlientiAdmin)
admin.site.register(HistPieraksti, HistPierakstiAdmin)
admin.site.register(HistAtteikumi)
