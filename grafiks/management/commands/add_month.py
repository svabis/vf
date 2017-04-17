# -*- coding: utf-8 -*-
import datetime # timedelta
import pytz     # to set timezone

from django.core.management.base import BaseCommand, CommandError
from grafiks.models import *    # import models


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

        tz = pytz.timezone('UTC') # Timezone info

        weekno = datetime.today().weekday()
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        today = today
        day = [0,1,2,3,4,5,6,0,1,2,3,4,5,6]

        plan = Planotajs.objects.all()
        d=0
        for n in range(0,4):
            for p in plan:
                if int(p.diena) == day[weekno]:
                    sakums = today + timedelta(days=d, hours=p.laiks.hour, minutes=p.laiks.minute)
                    new_sakums = sakums #.replace(tzinfo=tz)
                    new_graf = Grafiks(sakums=new_sakums, ilgums=p.ilgums, nodarbiba=p.nodarbiba, treneris=p.treneris, telpa=p.telpa, vietas=p.vietas)
                    new_graf.save()
                if int(p.diena) == day[weekno+1]:
                    sakums = today + timedelta(days=d + 1, hours=p.laiks.hour, minutes=p.laiks.minute)
                    new_sakums = sakums #.replace(tzinfo=tz)
                    new_graf = Grafiks(sakums=new_sakums, ilgums=p.ilgums, nodarbiba=p.nodarbiba, treneris=p.treneris, telpa=p.telpa, vietas=p.vietas)
                    new_graf.save()
                if int(p.diena) == day[weekno+2]:
                    sakums = today + timedelta(days=d + 2, hours=p.laiks.hour, minutes=p.laiks.minute)
                    new_sakums = sakums #.replace(tzinfo=tz)
                    new_graf = Grafiks(sakums=new_sakums, ilgums=p.ilgums, nodarbiba=p.nodarbiba, treneris=p.treneris, telpa=p.telpa, vietas=p.vietas)
                    new_graf.save()
                if int(p.diena) == day[weekno+3]:
                    sakums = today + timedelta(days=d + 3, hours=p.laiks.hour, minutes=p.laiks.minute)
                    new_sakums = sakums #.replace(tzinfo=tz)
                    new_graf = Grafiks(sakums=new_sakums, ilgums=p.ilgums, nodarbiba=p.nodarbiba, treneris=p.treneris, telpa=p.telpa, vietas=p.vietas)
                    new_graf.save()
                if int(p.diena) == day[weekno+4]:
                    sakums = today + timedelta(days=d + 4, hours=p.laiks.hour, minutes=p.laiks.minute)
                    new_sakums = sakums #.replace(tzinfo=tz)
                    new_graf = Grafiks(sakums=new_sakums, ilgums=p.ilgums, nodarbiba=p.nodarbiba, treneris=p.treneris, telpa=p.telpa, vietas=p.vietas)
                    new_graf.save()
                if int(p.diena) == day[weekno+5]:
                    sakums = today + timedelta(days=d + 5, hours=p.laiks.hour, minutes=p.laiks.minute)
                    new_sakums = sakums #.replace(tzinfo=tz)
                    new_graf = Grafiks(sakums=new_sakums, ilgums=p.ilgums, nodarbiba=p.nodarbiba, treneris=p.treneris, telpa=p.telpa, vietas=p.vietas)
                    new_graf.save()
                if int(p.diena) == day[weekno+6]:
                    sakums = today + timedelta(days=d + 6, hours=p.laiks.hour, minutes=p.laiks.minute)
                    new_sakums = sakums #.replace(tzinfo=tz)
                    new_graf = Grafiks(sakums=new_sakums, ilgums=p.ilgums, nodarbiba=p.nodarbiba, treneris=p.treneris, telpa=p.telpa, vietas=p.vietas)
                    new_graf.save()
            d += 7


