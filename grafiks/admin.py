from django.contrib import admin
from grafiks.models import *

class PlanotajsAdmin(admin.ModelAdmin):
    list_display = ['nodarbiba', 'treneris', 'diena', 'laiks', 'ilgums', 'telpa', 'vietas']
    list_filter = ['diena']

class GrafiksAdmin(admin.ModelAdmin):
    list_display = ['nodarbiba', 'treneris', 'sakums', 'ilgums', 'telpa', 'vietas']
    list_filter = ['sakums', 'nodarbiba']


admin.site.register(Grafiks, GrafiksAdmin)
admin.site.register(Planotajs, PlanotajsAdmin)
