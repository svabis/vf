# -*- coding: utf-8 -*-
import datetime # timedelta
import pytz	# to set timezone

from django.core.management.base import BaseCommand, CommandError
from grafiks.models import *	# import models

# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

#        tz = pytz.timezone('EET')       # Timezone info

        weekno = datetime.today().weekday()
        today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

        after_month = today + timedelta(days=28)
        nod = Grafiks.objects.filter( sakums__gt=after_month )

#        if not nod:
        plan = Planotajs.objects.all()
        for p in plan:
                if int(p.diena) == weekno:
                    if p.start_date <= after_month.date():	# ja nodarbība start_date ir pirms šodienas -->
                        sakums = today + timedelta(days=28, hours=p.laiks.hour, minutes=p.laiks.minute)
                        new_sakums = sakums #.replace(tzinfo=tz)
                        new_graf = Grafiks(sakums=new_sakums, ilgums=p.ilgums, nodarbiba=p.nodarbiba, treneris=p.treneris, telpa=p.telpa, vietas=p.vietas)
                        new_graf.save()

