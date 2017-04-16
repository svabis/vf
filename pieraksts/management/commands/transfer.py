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
        db = '/home/svabis/pieraksts.txt'
        tz = pytz.timezone('UTC')

        lines = [line.rstrip('\n') for line in open(db)]
        for line in lines:
            clients = Klienti.objects.all()
            l = line.split(';')

# l[0]+l[1] = time
# l[2] = Vārds Uzvārds
# l[3] = tel
# l[4] = e-mail
# l[5] = Nodarbība
            l[2] = slugify( l[2] ).lower()

           # 26,04,2017,19,00
           # Y M D H M
            time = l[0] + '.' + l[1]
            time = (datetime.datetime.strptime( time, '%d.%m.%Y.%H:%M') + datetime.timedelta(hours=-3)).replace(tzinfo=tz)

            nod = Nodarb_tips.objects.filter( nos = l[5] )
            graf_nod = Grafiks.objects.get( sakums = time, nodarbiba = nod )

            print str(graf_nod) + ' | ' + str(graf_nod.sakums) + ' | ' + str(graf_nod.treneris) + ' | ' + str(graf_nod.vietas)

            if graf_nod.vietas > 0:
                new = 0
                for c in clients:
                    if c.e_pasts == l[4] and c.vards == l[2]:
                       # klients jau eksiste
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

                if new == 0:
                   # Jauns klients
                    new_client = Klienti( vards = l[2], e_pasts = l[4], tel=l[3], pieteikuma_reizes = 1 )
                    new_client.save()

                    graf_nod.vietas -= 1
                    graf_nod.save()

                    pieraksts = Pieraksti( klients= new_client, nodarbiba = graf_nod ) # PIETEIKUMS --> ACCEPT
                    pieraksts.save()
                   # Pieraksts sekmigs

            else:
                print 'Nodarbiba pilna'
