# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.http.response import Http404	# ERRORR 404
from django.core.exceptions import ObjectDoesNotExist

from django.template.loader import get_template
from django.template import Context, RequestContext		# RequestContext <-- get user from request

from django.contrib.auth.models import User	# autorisation library
from django.contrib import auth			# autorisation library

from django.core.context_processors import csrf

from pieraksts.models import *
from grafiks.models import Grafiks
from grafiks.forms import PlanotajsForm

from pieraksts.forms import KlientsReceptionForm

# Pieraksta statistikas modulis
from statistika import day_stat

from slugify import slugify
from main import mail

import datetime
import pytz
today = datetime.date.today()
tz = pytz.timezone('UTC')

# ========================================================================================================

# !!!!! NODARBIBAS VĒSTURE !!!!!
def history(request):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    args.update(csrf(request)) # ADD CSRF TOKEN
    args['title'] = u'Izvēlies datumu'
    if request.POST:
        datums = request.POST.get('date', '')
        if datums != "":
            return redirect( 'hist_date', date=datums )
    return render_to_response( 'history.html', args )


def hist_date(request, date):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    datums = datetime.datetime.strptime( date, '%d/%m/%Y').date()
    dienas_nodarb = Grafiks.objects.filter(sakums__startswith=datums).order_by('sakums') # datuma nodarbibas

    args.update(csrf(request)) # ADD CSRF TOKEN
    args['date'] = date
    args['title'] = datums
    args['data'] = dienas_nodarb
    return render_to_response( 'hist_date.html', args )

def hist_date_kli(request, date, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    args.update(csrf(request)) # ADD CSRF TOKEN
    klienti = Grafiks.objects.get(id=g_id).hist.all()
    datums = datetime.datetime.strptime( date, '%d/%m/%Y').date()

    args['date'] = date
    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'hist_date_kli.html', args )

def hist_date_cancel(request, date, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    args.update(csrf(request)) # ADD CSRF TOKEN
    klienti = Grafiks.objects.get(id=g_id).hist_cancel.all()
    datums = datetime.datetime.strptime( date, '%d/%m/%Y').date()

    args['date'] = date
    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'hist_date_cancel.html', args )
