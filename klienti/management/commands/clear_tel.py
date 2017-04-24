# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from klienti.models import *	# import models


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

        klienti = Klienti.objects.all()

        for k in klienti:
            if k.tel.startswith('+371 '):
                    print k.tel[5:]
                    k.tel = k.tel[5:]
                    k.save()

            elif k.tel.startswith('+371'):
                    print k.tel[4:]
                    k.tel = k.tel[4:]
                    k.save()

