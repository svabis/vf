# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from klienti.models import *	# import models

from klienti.models import Klienti
from pieraksts.models import Pieraksti
from grafiks.models import *

from datetime import datetime
from datetime import timedelta

from main import mail

# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):
        timenow = datetime.now()
        tomorow = timenow + timedelta(days=1)

        if timenow.hour == 20:
            start = tomorow.replace(hour=0, minute=0, second=0, microsecond=0)
            end = tomorow.replace(hour=12, minute=59, second=0, microsecond=0)
            timerange = [start, end]

        if timenow.hour == 8:
            start = timenow.replace(hour=13, minute=0, second=0, microsecond=0)
            end = timenow.replace(hour=23, minute=30, second=0, microsecond=0)
            timerange = [start, end]

        graf = Grafiks.objects.filter( sakums__range = timerange )
        count = 0
        for g in graf:
#            print g
            klienti = Grafiks.objects.get(id=g.id).nod.all()
            for k in klienti:
                count += 1
                try:
                    mail.send_remind(k.klients.e_pasts, str(g.nodarbiba), g.sakums, k.atteikuma_kods)
                except:
                    pass
#        print count
