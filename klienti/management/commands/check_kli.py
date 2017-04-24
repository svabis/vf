# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from klienti.models import *	# import models


# COMAND BEGIN
class Command(BaseCommand):
    def handle(self, *args, **options):

        klienti = Klienti.objects.all()

        name = 0
        temp = klienti[0].vards
        for k in klienti:
            if k.vards == temp:
                name += 1

        tel = 0
        temp = klienti[0].tel
        for k in klienti:
            if k.tel == temp:
                tel += 1

        mail = 0
        temp = klienti[0].e_pasts
        for k in klienti:
            if k.e_pasts == temp:
                mail += 1

        print 'vārdu dublikāti: '+ str(name -1)
        print 'e-pastu dublikāti: ' + str(mail -1)
        print 'teleonu dublikāti: ' + str(tel -1)

