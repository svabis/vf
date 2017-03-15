from django.contrib import admin
from grafiks.models import *

class PlanotajsAdmin(admin.ModelAdmin):
    list_display = ['nodarbiba', 'treneris', 'sakums', 'ilgums', 'telpa', 'vietas']
#    list_filter = ['nodarb', 'treneris']

class GrafiksAdmin(admin.ModelAdmin):
    list_display = ['nodarbiba', 'treneris', 'sakums', 'ilgums', 'telpa', 'vietas']
    list_filter = ['nodarbiba', 'sakums']


admin.site.register(Grafiks, GrafiksAdmin)
admin.site.register(Planotajs, PlanotajsAdmin)
