from django.contrib import admin
from pieraksts.models import *


class PierakstiAdmin(admin.ModelAdmin):
    list_display = ['pieraksta_laiks', 'klients', 'nodarbiba', 'atteikuma_kods']
    list_filter = ['pieraksta_laiks']

class AtteikumiAdmin(admin.ModelAdmin):
    list_display = ['pieraksta_laiks', 'ateikuma_laiks', 'klients', 'nodarbiba']
    list_filter = ['ateikuma_laiks']


admin.site.register(Pieraksti, PierakstiAdmin)
admin.site.register(Atteikumi, AtteikumiAdmin)
