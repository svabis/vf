from django.contrib import admin
from pieraksts.models import *

class PierakstiAdmin(admin.ModelAdmin):
    list_display = ['pieraksta_laiks', 'klients', 'nodarbiba']


admin.site.register(Pieraksti, PierakstiAdmin)

