from django.contrib import admin
from pieraksts.models import *


class PierakstiAdmin(admin.ModelAdmin):
    list_display = ['pieraksta_laiks', 'klients', 'nodarbiba', 'atteikuma_kods']

class AtteikumiAdmin(admin.ModelAdmin):
    list_display = ['ateikuma_laiks', 'klients', 'nodarbiba']


admin.site.register(Pieraksti, PierakstiAdmin)
admin.site.register(Atteikumi, AtteikumiAdmin)
