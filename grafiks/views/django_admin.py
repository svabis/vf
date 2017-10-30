# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from django.db.models import Q
#from django.contrib.postgres.search import SearchVector # SEARCH

from klienti.models import *
#from grafiks.models import Grafiks, Planotajs
#from grafiks.forms import *
#from nodarb.models import *

#from main import mail

import datetime
import pytz
today = datetime.date.today()
tz = pytz.timezone('UTC')

import os

# ========================================================================================================

# !!!!! Klientu saraksts !!!!!
def klienti(request):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    args.update(csrf(request))

    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args['super'] = True

    if request.POST: # Search...
        to_find = request.POST.get('search', '')

        args['klienti'] = Klienti.objects.filter( Q( vards__icontains = to_find ) | Q( e_pasts__icontains = to_find ) | Q( tel__icontains = to_find ) ).order_by('vards')
        return render_to_response ( 'klienti.html', args )

    args['klienti'] = Klienti.objects.all().order_by('vards')
    return render_to_response ( 'klienti.html', args )


