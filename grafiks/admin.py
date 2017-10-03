from django.contrib import admin
from grafiks.models import *

class PlanotajsAdmin(admin.ModelAdmin):
    list_display = ['nodarbiba', 'treneris', 'diena', 'laiks', 'ilgums', 'telpa', 'vietas', 'start_date', 'end_date']
    list_filter = ['diena', 'nodarbiba']

class GrafiksAdmin(admin.ModelAdmin):
    list_display = ['nodarbiba', 'treneris', 'sakums', 'ilgums', 'telpa', 'vietas']
    list_filter = ['sakums', 'nodarbiba']


admin.site.register(Grafiks, GrafiksAdmin)
admin.site.register(Planotajs, PlanotajsAdmin)
