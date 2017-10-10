from django.contrib import admin
from log.models import *


class DayPierStatAdmin(admin.ModelAdmin):
    list_display = ['x', 'y']
#    list_filter = ['pirmais_pieteikums', 'pedejais_pieteikums']
#    search_fields = ['vards', 'e_pasts', 'tel']
#    exclude = ['pirmais_pieteikums', 'pedejais_pieteikums', 'atteikuma_reizes', 'pieteikuma_reizes']

admin.site.register(DayPierStat, DayPierStatAdmin)

