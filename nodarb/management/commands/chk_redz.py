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
        start = datetime.datetime(today.year, today.month, today.day, today.hour, today.minute)
        end = today.replace(hour=23, minute=59, second=59) + datetime.timedelta(days=28)
#        print start
#        print end

       # Hide all Nodarbības
        nod = Nodarb_tips.objects.all()
        for n in nod:
            n.redz = False
            n.save()

       # Get grafiks entries for 4 weeks
        graf = Grafiks.objects.filter(sakums__range=( start, end))
        temp = []
        for g in graf:
            n = g.nodarbiba
            temp.append(n)

#        print graf.count() # grafiks count

        redz_fakt = list(set(temp))
#        print len(redz_fakt)

        for r in redz_fakt:
#            print r
            n = Nodarb_tips.objects.get( nos=r )
            n.redz = True
            n.save()
