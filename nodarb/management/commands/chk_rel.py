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

       # All relations
        rel_exist = Tren_nodarb.objects.all()

       # Get grafiks entries for 4 weeks
        graf = Grafiks.objects.filter(sakums__range=( start, end))
        temp_rel = []
        for g in graf:
            t = g.treneris
            n = g.nodarbiba
            temp_rel.append([n,t])

        rel_fakt = set(tuple(element) for element in temp_rel) # extract unique from all
        print graf.count() # grafiks count
        print len(rel_fakt) # relation count

       # Create relations if not exist
        print 'creating relations...'
        temp_rel = []
        for r in list(rel_fakt):
            try:
                obj = Tren_nodarb.objects.get( nodarb=r[0], treneris=r[1] )
                temp_rel.append(obj) # add to list
            except:
                new_rel = Tren_nodarb( nodarb=r[0], treneris=r[1])
                new_rel.save()
                temp_rel.append(new_rel) # add to list
                print r
        print '...done\n'

       # Remove not needed relations
        print 'deleting unused relations...'
        temp_rel2 = []
        for r in rel_exist:
            temp_rel2.append(r)

        unused = list(set(temp_rel2) - set(temp_rel))
        for u in unused:
            u.delete()
            print u
        print '...done\n'
