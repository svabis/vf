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

# !!!!! SUPERUSER NODARBIBAS ATCELSHANA NEDELAS IZVELE !!!!!
def graf_list(request):
    username = auth.get_user(request)
    if username.is_superuser:
        args = {}
        args['super'] = True
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
        args['super'] = True
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
        args['w_id'] = w_id
        args['data'] = grafiks
        return render_to_response ( 'nod_plan.html', args )
    return redirect('/reception/login/')

def graf_cancel(request, w_id, g_id):
    username = auth.get_user(request)
    if username.is_superuser:
        args = {}
        args['super'] = True
        nodarb = Grafiks.objects.get(id=g_id)
        klienti = nodarb.nod.all()
        for k in klienti:
            try:
                mail.send_cancel(k.klients.e_pasts, nodarb.sakums, nodarb.nodarbiba.nos) #SEND CANCEL MAIL
# !!!!! INSERT DELETE PIERAKSTS !!!!!
            except:
                pass

        nodarb.delete()
        return redirect ( 'nod_plan', w_id=w_id )
    return redirect('/reception/login/')

# ========================================================================================================

# !!!!! SUPERUSER PIEVIENOT GRAFIKAM JAUNU NODARBIBU !!!!!
def graf_add(request):
    username = auth.get_user(request)
    if username.is_superuser:
        args = {}
        args.update(csrf(request))      # ADD CSRF TOKEN
        args['super'] = True
        args['form'] = PlanotajsForm

        return render_to_response('add_plan.html', args)
    return redirect('/reception/login/')

# ========================================================================================================

