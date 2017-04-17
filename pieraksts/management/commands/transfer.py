# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone

from nodarb.models import *
from klienti.models import Klienti
from grafiks.models import Grafiks
from pieraksts.models import *

from slugify import slugify

# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
       db = '/home/svabis/import.txt'
       tz = pytz.timezone('UTC')
       lines = [line.rstrip('\n') for line in open(db)]

#       if True:
#           line = lines[0]
       for line in lines:
           clients = Klienti.objects.all()
           l = line.split(';')
           l[2] = slugify( l[2] ).lower()
           error = 0

           time = l[0] + '.' + l[1]
           time = (datetime.datetime.strptime( time, '%d.%m.%Y.%H:%M') + datetime.timedelta(hours=-3)).replace(tzinfo=tz)

           try:
             nod = Nodarb_tips.objects.filter( nos = l[5] )
             graf_nod = Grafiks.objects.get( sakums = time, nodarbiba = nod )
#             print str(graf_nod) + ' | ' + str(graf_nod.sakums) + ' | ' + str(graf_nod.treneris) + ' | ' + str(graf_nod.vietas)

             if graf_nod.vietas > 0:
                new = 0
                for c in clients:
                    if c.e_pasts == l[4] and c.vards == l[2]:
                       # klients jau eksiste
                        nod_start = getattr( graf_nod, 'sakums')
                        nod_end = getattr( graf_nod, 'sakums') + datetime.timedelta(minutes=int(getattr( graf_nod, 'ilgums')))

                        nod_date = nod_start.date()
                        date_nod = Grafiks.objects.filter( sakums__startswith = nod_date ).order_by('sakums')

                        count = 0
                        for d in date_nod:
                            end = d.sakums + datetime.timedelta(minutes=int(d.ilgums))
                            Overlap = max(nod_start, d.sakums) < min(nod_end, end)
                            if Overlap == True:
                                try:
                                    pieraksti_nodarb = Pieraksti.objects.get( klients = c, nodarbiba = d )
                                    count += 1
                                except Pieraksti.DoesNotExist:
                                    pass
                                except:
                                    count += 1

                        if count != 0:
                            result = False
                        else:
                            result = True

                        if result == True: # pieraksts nepārklājas

                            c.pieteikuma_reizes += 1
                            c.pedejais_pieteikums = datetime.datetime.now().replace(tzinfo=tz)
                            c.tel = l[3]
                            c.save()
                            new += 1

                            graf_nod.vietas -= 1
                            graf_nod.save()

                            pieraksts = Pieraksti( klients = c, nodarbiba = graf_nod ) # PIETEIKUMS --> ACCEPT
                            pieraksts.save()
                        # Pieraksts sekmigs
#                       else:
#                           print 'OVERLAP'
#                           print line

                if new == 0:
                  # Jauns klients
                   new_client = Klienti( vards = l[2], e_pasts = l[4], tel=l[3], pieteikuma_reizes = 1 )
                   new_client.save()

                   graf_nod.vietas -= 1
                   graf_nod.save()

                   pieraksts = Pieraksti( klients= new_client, nodarbiba = graf_nod ) # PIETEIKUMS --> ACCEPT
                   pieraksts.save()
                  # Pieraksts sekmigs

           except:
               error += 1
               print 'ERROR'
               print line
