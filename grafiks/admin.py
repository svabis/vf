from django.contrib import admin
from grafiks.models import *

class PlanotajsAdmin(admin.ModelAdmin):
    list_display = ['nodarbiba', 'treneris', 'sakums', 'telpa', 'vietas']
#    list_filter = ['nodarb', 'treneris']


admin.site.register(Grafiks)
admin.site.register(Planotajs, PlanotajsAdmin)
