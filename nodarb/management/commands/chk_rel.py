# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from grafiks.models import *
from nodarb.models import *


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

       # Define 4 week boundries
        import datetime
        today = datetime.datetime.now()
        start = datetime.datetime(today.year, today.month, today.day)
        end = today.replace(hour=23, minute=59, second=59) + datetime.timedelta(days=28)

       # Delete all relations
        Tren_nodarb.objects.all().delete()

       # get grafiks entries for 4 weeks
        graf = Grafiks.objects.filter(sakums__range=( start, end))
        temp_rel = []
        for g in graf:
            t = g.treneris
            n = g.nodarbiba
            temp_rel.append([n,t])

        rel_fakt = set(tuple(element) for element in temp_rel)
        print graf.count() # total count
        print len(rel_fakt) # unique count
        print
        for r in list(rel_fakt):
            new_rel = Tren_nodarb( nodarb=r[0], treneris=r[1])
            new_rel.save()
            print r

#        print
       # Relacijas Objects all
#        rel_obj = []

#        for t in Tren_nodarb.objects.all():
#            rel_obj.append(t)
#        for r in list(set(rel_obj)):
#            print r
