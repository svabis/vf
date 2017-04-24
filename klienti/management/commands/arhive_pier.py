# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from klienti.models import *	# import models
from pieraksts.models import *

import datetime

# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

        pier = Pieraksti.objects.all()

        today = datetime.date.today() - datetime.timedelta(days=4)
        print today

        count = 0
        for p in pier:
            if  p.nodarbiba.sakums.date() < today:
                hist = HistPieraksti( pieraksta_laiks = p.pieraksta_laiks, klients = p.klients, nodarbiba = p.nodarbiba )
                hist.save()

#                print p.nodarbiba.sakums
                p.delete()
