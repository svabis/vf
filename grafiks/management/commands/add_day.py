# -*- coding: utf-8 -*-
import datetime # timedelta
from datetime import date # to test if end_date is date object
import pytz	# to set timezone

from django.core.management.base import BaseCommand, CommandError
from grafiks.models import *	# import models

# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
#        tz = pytz.timezone('EET')       # Timezone info
        weekno = datetime.today().weekday()
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

        after_month = today + timedelta(days=28+28)
        nod = Grafiks.objects.filter( sakums__gt=after_month )

        plan = Planotajs.objects.all()
        for p in plan:
            if int(p.diena) == weekno:
               # ja nodarbība start_date ir pirms šodienas (ieskaitot) -->
                if p.start_date <= after_month.date():
                   # un ja nodarbība end_date nav datuma objekts -->
                    if isinstance(p.end_date, date) == False:
                        sakums = today + timedelta(days=28+28, hours=p.laiks.hour, minutes=p.laiks.minute)
                        new_sakums = sakums #.replace(tzinfo=tz)
                        new_graf = Grafiks(sakums = new_sakums,
                                           ilgums = p.ilgums,
                                           nodarbiba = p.nodarbiba,
                                           treneris = p.treneris,
                                           telpa = p.telpa,
                                           vietas = p.vietas)
                        new_graf.save()
                   # vai arī end_date ir datuma objekts un tas ir pēc tekošā datuma -->
                    elif p.end_date >= after_month.date():
                        sakums = today + timedelta(days=28+28, hours=p.laiks.hour, minutes=p.laiks.minute)
                        new_sakums = sakums #.replace(tzinfo=tz)
                        new_graf = Grafiks(sakums = new_sakums,
                                           ilgums = p.ilgums,
                                           nodarbiba = p.nodarbiba,
                                           treneris = p.treneris,
                                           telpa = p.telpa,
                                           vietas = p.vietas)
                        new_graf.save()
                   # end_date jau ir pagājis
                    elif p.end_date < datetime.today().date():
                        p.delete()



