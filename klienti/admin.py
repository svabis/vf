from django.contrib import admin
from klienti.models import Klienti


class KlientiAdmin(admin.ModelAdmin):
    list_display = ['vards', 'e_pasts', 'tel', 'pirmais_pieteikums', 'pedejais_pieteikums', 'pieteikuma_reizes', 'atteikuma_reizes']
    list_filter = ['pirmais_pieteikums', 'pedejais_pieteikums']

admin.site.register(Klienti, KlientiAdmin)
