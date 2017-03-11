from django.contrib import admin
from nodarb.models import *


class Nodarb_tipsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nos',),}
    list_display = ['nos', 'slug', 'apraksts']


class TrenerisAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('vards',),}
    list_display = ['vards', 'slug', 'apraksts']


class Tren_nodarbAdmin(admin.ModelAdmin):
    list_display = ['nodarb', 'treneris']
    list_filter = ['nodarb', 'treneris']

class TelpaAdmin(admin.ModelAdmin):
    list_display = ['telpa']

admin.site.register(Nodarb_tips, Nodarb_tipsAdmin)
admin.site.register(Treneris, TrenerisAdmin)
admin.site.register(Tren_nodarb, Tren_nodarbAdmin)
admin.site.register(Telpa, TelpaAdmin)
