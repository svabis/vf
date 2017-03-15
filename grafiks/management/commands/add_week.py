# -*- coding: utf-8 -*-
import datetime # timedelta
import pytz	# to set timezone

from django.core.management.base import BaseCommand, CommandError
from grafiks.models import Grafiks	# import model


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

