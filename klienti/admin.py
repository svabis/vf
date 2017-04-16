from django.contrib import admin
from klienti.models import Klienti


class KlientiAdmin(admin.ModelAdmin):
    list_display = ['vards', 'e_pasts', 'tel','pirmais_pieteikums', 'pedejais_pieteikums', 'pieteikuma_reizes', 'atteikuma_reizes']
    list_filter = ['pirmais_pieteikums', 'pedejais_pieteikums']
    search_fields = ['vards', 'e_pasts', 'tel']
    exclude = ['pirmais_pieteikums', 'pedejais_pieteikums', 'atteikuma_reizes', 'pieteikuma_reizes']

admin.site.register(Klienti, KlientiAdmin)
