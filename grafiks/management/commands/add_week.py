# -*- coding: utf-8 -*-
import datetime # timedelta
import pytz	# to set timezone

from django.core.management.base import BaseCommand, CommandError
from grafiks.models import Grafiks	# import model


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

#		DemoJobs.objects.all().delete()
# FILL DEMO LIST
#			P              S            S

#                                   Y   M  D   H   M
        new_date = datetime.datetime.now().replace(hour=7, minute=30, second=0) + datetime.timedelta(days=2)
        print new_date

        new_item = Grafiks()

        date = datetime.datetime(2009, 10, 5, 18, 00)

        time = [10, 30, 90]

        jobs = ['viens darbs', 'nākamais darbs', 'svarīgs darbs', 'nesvarīgs darbs', 'materiālu iegāde',
			'iepirkt lietas', 'uzkopt teritoriju', 'atvest nopirktās lietas', 'darīt darbus', 'DEMO ieraksts',
			'stādīšanas darbi', 'nespiegot', '	aizskrūvēt burciņu', 'Demo ieraksts ar garu tekstu, jeb daudz simboliem vienā rindā, tā teikt "ļoti" garš ieraksts']

        zone = ['maja', 'lapene', 'IT', 'darzs', 'cits',
			'maja', 'darzs', 'cits', 'IT', 'lapene',
			'koki', 'cits', 'maja', 'zogs']

        type = ['JADARA', 'JADARA', 'SVARIGI', 'VEST', 'JAPERK',
			'JAPERK', 'JADARA', 'VEST', 'SVARIGI', 'JAPERK',
			'JADARA', 'SVARIGI', 'JADARA', 'JAPERK']

#        for nr in range (0,14):
#            new_item = Grafiks(
#                jobs_date_added = datetime.date.today() - datetime.timedelta(days=days[nr]),
#                jobs_descr = jobs[nr],
#                jobs_zone = zone[nr],
#                jobs_type = type[nr])
#            nwe_item.save()
