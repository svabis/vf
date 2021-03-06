# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view

from django.contrib import auth			# autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from grafiks.models import Grafiks

import datetime
import pytz
today = datetime.date.today()
tz = pytz.timezone('UTC')


# !!!!! DATUMA IZVĒLE !!!!!
def history(request):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args['admin'] = True
    if username.is_superuser:
        args['django'] = True

    args.update(csrf(request)) # ADD CSRF TOKEN
    if request.POST:
        datums = request.POST.get('date', '')
        if datums != "":
            return redirect( 'hist_date', date=datums )
    return render_to_response( 'history.html', args )


# !!!!! DIENAS VĒSTURE !!!!!
def hist_date(request, date):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    username = auth.get_user(request)
    if username.is_superuser:
        args['django'] = True
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args['admin'] = True

    datums = datetime.datetime.strptime( date, '%d/%m/%Y').date()
    dienas_nodarb = Grafiks.objects.filter(sakums__startswith=datums).order_by('sakums') # datuma nodarbibas

    args.update(csrf(request)) # ADD CSRF TOKEN
    args['date'] = date
    args['title'] = datums
    args['data'] = dienas_nodarb
    return render_to_response( 'hist_date.html', args )


# !!!!! NODARBIBAS PIERAKSTI !!!!!
def hist_date_kli(request, date, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    username = auth.get_user(request)
    if username.is_superuser:
        args['django'] = True
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args['admin'] = True

    args.update(csrf(request)) # ADD CSRF TOKEN
    klienti = Grafiks.objects.get(id=g_id).hist.all()
    datums = datetime.datetime.strptime( date, '%d/%m/%Y').date()

    args['date'] = date
    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'hist_date_kli.html', args )


# !!!!! NODARBIBAS ATTEIKUMI !!!!!
def hist_date_cancel(request, date, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    username = auth.get_user(request)
    if username.is_superuser:
        args['django'] = True
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args['admin'] = True

    args.update(csrf(request)) # ADD CSRF TOKEN
    klienti = Grafiks.objects.get(id=g_id).hist_cancel.all()
    datums = datetime.datetime.strptime( date, '%d/%m/%Y').date()

    args['date'] = date
    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'hist_date_cancel.html', args )
