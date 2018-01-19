# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth			# autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf
from django.db.models import Q

from klienti.models import Klienti
from pieraksts.models import *
#from grafiks.models import Grafiks

#from pieraksts.forms import KlientsReceptionForm

from slugify import slugify

import datetime
import pytz
today = datetime.date.today()
tz = pytz.timezone('UTC')

# ========================================================================================================
# !!!!! Klientu saraksts/meklēšana !!!!!
def klienti(request, search=''):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    args.update(csrf(request))

    username = auth.get_user(request)
    if username.is_superuser:
        args['django'] = True
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args['admin'] = True

    if request.POST: # POST Search --> SEARCH FROM POST
        to_find = request.POST.get('search', '')
        args['klienti'] = Klienti.objects.filter( Q( vards__icontains = to_find ) | Q( e_pasts__icontains = to_find ) | Q( tel__icontains = to_find ) ).order_by('vards')
        args['search'] = to_find
        return render_to_response ( 'klienti.html', args )

    elif search != '': # NO POST and search != "" --> SEARCH FROM VARIABLE
        search = str(search)
        args['klienti'] = Klienti.objects.filter( Q( vards__icontains = search ) | Q( e_pasts__icontains = search ) | Q( tel__icontains = search ) ).order_by('vards')
        args['search'] = search
        return render_to_response ( 'klienti.html', args )

    args['klienti'] = Klienti.objects.all().order_by('vards')
    args['search'] = ''
    return render_to_response ( 'klienti.html', args )


# !!!!! Klienta kartiņas labošana !!!!!
def klients_edit(request):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    username = auth.get_user(request)

    if request.POST: # Edit Post Submited...
       # klienta Modal dati + search paramets
        search = request.POST.get('search', '')

        k_id = int(request.POST.get('k_id', ''))
        k_vards = request.POST.get('vards', '')
        k_e_pasts = request.POST.get('e_pasts', '')
        k_tel = request.POST.get('tel', '')

       # get Klients object
        kli = Klienti.objects.get(id=k_id)

        kli.vards = k_vards
        kli.e_pasts = k_e_pasts
        kli.tel = k_tel
        kli.save()
    if search == '':
        return redirect ( 'klienti' )
    return redirect ( 'klienti', search=search )


# ========================================================================================================
# !!!!! Klienta pierakstu/atteikumu saraksts !!!!!
def klients_list(request, k_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    args.update(csrf(request))

    username = auth.get_user(request)
    if username.is_superuser:
        args['django'] = True
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args['admin'] = True

    kli = Klienti.objects.get( id = int(k_id) )
    args['klients'] = kli
    args['dati'] = Pieraksti.objects.filter( klients = kli ).order_by('nodarbiba')

    return render_to_response ( 'klienti_data.html', args )
