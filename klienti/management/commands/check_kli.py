# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from klienti.models import *	# import models

from pieraksts.models import Pieraksti

# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
        klienti = Klienti.objects.all()
# !!! VARDI !!!
        v = []
        name = 0
        for n in range( 0, len(klienti) ):
            temp = klienti[n].vards
            for m in range( 0, len(klienti) ):
                if n != m:
                    if klienti[m].vards == temp:
                        name += 1
                        v.append( klienti[m].vards )

#        print 'vārdu dublikāti: '+ str(name)
#        v = sorted(v)
#        for n in range( 0, len(v) ):
#            print str(n+1) + '\t' + str(v[n]) #+ '\t' + str(n.e_pasts) + '\t' + str(n.tel)

# !!! TELEFONI !!!
        t = []
        tel = 0
        for n in range( 0, len(klienti) ):
            temp = klienti[n].tel
            for m in range( 0, len(klienti) ):
                if n != m:
                    if klienti[m].tel == temp:
                        tel += 1
                        t.append( klienti[m].tel )
                        print str(klienti[m]) + '\t' + str(klienti[m].e_pasts) + '\t' + str(klienti[m].tel)

        print 'teleonu dublikāti: ' + str(tel)
        t = sorted(t)
        for n in range( 0, len(t) ):
            print str(n+1) + '\t' + str(t[n])


# !!! E-PASTI !!!
        mail = 0
        temp = klienti[0].e_pasts
        for k in klienti:
            if k.e_pasts == temp:
                mail += 1

#        print 'e-pastu dublikāti: ' + str(mail -1)

#        c = Klienti.objects.filter( vards='natalja-jevdokimova' )
#        print c

#        e = Klienti.objects.filter( e_pasts = 'nuka_x@inbox.lv' )
#        print e
#        p1 = Pieraksti.objects.get( id=3354 )
#        print p1.pieraksta_laiks
#        p2 = Pieraksti.objects.get( id=3355 )
#        print p2.pieraksta_laiks


