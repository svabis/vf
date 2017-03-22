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

import datetime
#from datetime import date
today = datetime.date.today()


# !!!!! LOGIN !!!!!
def login(request):
        args = {}       # create new argument list
        args.update(csrf(request))      # encript data
        args['heading'] = "Ielogošanās sistēmā"

        if request.POST:        # actions if login Form is submitted
                username        = request.POST.get('username', '')      # usermname <= get variable from Form (name="username"), if not leave blank
                password        = request.POST.get('password', '')      # password <= get variable from Form (name="password"), if not leave blank
                user            = auth.authenticate( username = username, password = password ) # new variable --> user from auth system

                if user is not None:    # auth return None if this user does not exit, if not then:
                        auth.login( request, user )     # authorizate user from Form
		        return redirect ("/reception/")

                else:   # if user does not exist:
                        args['login_error']     = "Lietotājs nav atrasts"
                        return render_to_response ( 'login.html', args )

        else:   # actions if activated hyperlink to login Form
                return render_to_response ( 'login.html', args )

# ========================================================================================================

# !!!!! VISAS DIENAS NODARBIBAS !!!!!
def main(request):
    if auth.get_user(request).get_username() == '': # IF NO USER --> 
        return redirect ("/reception/login/")
    sodien = Grafiks.objects.filter(sakums__startswith=today).order_by('sakums')
    args = {}
    args['title'] = today
    args['data'] = sodien
    return render_to_response( 'day_data.html', args )


# !!!!! KONKRETA DIENAS NODARBIBA !!!!!
def nod_list(request, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')

    klienti = Grafiks.objects.get(id=g_id).nod.all()
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'kli_data.html', args )


# !!!!! NODARBIBAS ATEIKUMI !!!!!
def cancel_list(request, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')

    klienti = Grafiks.objects.get(id=g_id).ateikt.all()
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'cancel_data.html', args )

# ========================================================================================================

# !!!!! SUPERUSER NODARBIBAS ATCELSHANA NEDELAS IZVELE !!!!!
def graf_list(request):
    username = auth.get_user(request)
    if username.is_superuser:
        args = {}
        weeks = []
        weeks.append(today)

        next = today + datetime.timedelta( days=7 - int( today.weekday()) ) # next week monday
        for _ in range (0,4): # add 4 weeks in row
            weeks.append(next)
            next = next + datetime.timedelta(days=7)

        args['week'] = weeks
        return render_to_response ( 'nod_plan.html', args )
    return redirect('/reception/login/')


# !!!!! SUPERUSER NODARBIBAS ATCELSHANA NEDELAS IZVELE !!!!!
def week_list(request, w_id):
    username = auth.get_user(request)
    if username.is_superuser:
        args = {}
        weeks = []
        weeks.append(today)
        next = today + datetime.timedelta( days=7 - int( today.weekday()) ) # next week monday
        for _ in range (0,4): # add 4 weeks in row
            weeks.append(next)
            next = next + datetime.timedelta(days=7)

       # check if full week
        if int(w_id) == 0:
            days = 7 - int( today.weekday())
        else:
            days = 7

        grafiks = []
        for d in range (0,days): # add 7 days in row
            try:
                gr = Grafiks.objects.filter(sakums__startswith=( weeks[int(w_id)] + datetime.timedelta( days=d ))).order_by('sakums')
                grafiks.append(gr)
            except: # if day is empty
                pass
#                gr = []

        args['data'] = grafiks
        return render_to_response ( 'nod_plan.html', args )
    return redirect('/reception/login/')

