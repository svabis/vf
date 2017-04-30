# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from klienti.models import *	# import models
from pieraksts.models import *

import datetime

# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

# !!! PIERAKSTI !!!
        pier = Pieraksti.objects.all()
        today = datetime.date.today() # - datetime.timedelta(days=1)
        count = 0
        for p in pier:
            if  p.nodarbiba.sakums.date() < today:
                hist = HistPieraksti( pieraksta_laiks = p.pieraksta_laiks, klients = p.klients, nodarbiba = p.nodarbiba )
                hist.save()
                p.delete()


# !!! ATTEIKUMI !!!
        cancel = Atteikumi.objects.all()
        today = datetime.date.today() # - datetime.timedelta(days=1)
        for c in cancel:
            if  c.nodarbiba.sakums.date() < today:
                hist = HistAtteikumi( ateikuma_laiks = c.ateikuma_laiks, klients = c.klients, nodarbiba = c.nodarbiba )
                hist.save()
                c.delete()

