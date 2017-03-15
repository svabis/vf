# -*- coding: utf-8 -*-
import datetime # timedelta
import pytz	# to set timezone

from django.core.management.base import BaseCommand, CommandError
from grafiks.models import *	# import models


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

        weekno = datetime.datetime.today().weekday()
#        day = [0,1,2,3,4,5,6]
#        day = [13,14,15,16,17,18,19]

        plan = Planotajs.objects.all()
        for p in plan:
            if p.diena == weekno:
                new_sakums = p.sakums + datetime.timedelta(days=7)
                new_graf = Grafiks(sakums=new_sakums, ilgums=p.ilgums, nodarbiba=p.nodarbiba, treneris=p.treneris, telpa=p.telpa, vietas=p.vietas)
                new_graf.save()
                print p

