# -*- coding: utf-8 -*-
import os       # for work with filesystem
import datetime # for file create field

from statistika.models import *


# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    def handle(self, *args, **options):
       logfile = '/home/svabis/stat'
       stat = DayPierStat.objects.all()
       x = []
       y = []

       for s in stat:
           x.append(s.x)
           y.append(s.y)
           s.delete()

       with open(logfile, "w") as myfile:

           for n in range(0, len(x)):
               myfile.write( str(x[n]) + ' | ' + str(y[n]) + '\n' )

       myfile.close()
