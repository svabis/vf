from django.contrib import admin
from log.models import *


class LogAdmin(admin.ModelAdmin):
    list_display = ['log_user', 'log_date', 'log_event', 'log_event_data']
    list_filter = ['log_user', 'log_date', 'log_event']
#    search_fields = ['vards', 'e_pasts', 'tel']
#    exclude = ['pirmais_pieteikums', 'pedejais_pieteikums', 'atteikuma_reizes', 'pieteikuma_reizes']

admin.site.register(Log, LogAdmin)

