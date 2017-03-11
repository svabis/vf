from django.contrib import admin
from klienti.models import Klienti


class KlientiAdmin(admin.ModelAdmin):
    list_display = ['vards', 'e_pasts', 'tel', 'pirmais_pieteikums', 'pedejais_pieteikums', 'pieteikuma_reizes']
    list_filter = ['pirmais_pieteikums', 'pedejais_pieteikums', 'pieteikuma_reizes']

admin.site.register(Klienti, KlientiAdmin)
