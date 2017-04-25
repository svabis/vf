# -*- coding: utf-8 -*-
import datetime # timedelta
import pytz     # to set timezone

from django.core.management.base import BaseCommand, CommandError
from grafiks.models import *    # import models
from pieraksts.models import *    # import models
from klienti.models import *    # import models


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):


        weekno = datetime.today().weekday()
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        today = today
        day = [0,1,2,3,4,5,6,0,1,2,3,4,5,6]

        grafiks = Grafiks.objects.all()

        for g in grafiks:
            d = g.sakums.weekday()
            plan_day = Planotajs.objects.filter( diena=d )

            print plan_day


#        d = 0
#        if True:
#        for d in range(0,4):
#            for p in plan:
#                if int(p.diena) == day[weekno]:
#                    new_sakums = today + timedelta( days=d, hours=p.laiks.hour, minutes=p.laiks.minute )
#                    graf = Grafiks.objects.filter( sakums=new_sakums )
#                    print graf[0].nodarbiba
#                    pier =  Pieraksti.objects.filter( nodarbiba = graf[0] )
#                    dif = p.vietas - len(pier)
#                    if graf[0].vietas != dif:
#                        print graf[0]
#                        print 'vietas planotājs - ' + str(p.vietas)
#                        print 'grafiks + starpība - ' + str(graf[0].vietas + dif)
#                        print dif
#                    for pi in pier:
#                        print pi.klients
#                    print graf[0].vietas
#                    print p.vietas
#                d += 1

