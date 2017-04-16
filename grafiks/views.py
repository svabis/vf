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

from main import mail

import datetime
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
                        args['super'] = True
		        return redirect ("/reception/")

                else:   # if user does not exist:
                        args['login_error']     = "Lietotājs nav atrasts"
                        return render_to_response ( 'login.html', args )

        else:   # actions if activated hyperlink to login Form
                return render_to_response ( 'login.html', args )

# !!!!! LOG OUT !!!!!
def logout(request):
    auth.logout(request)
    return redirect('/reception/')

# ========================================================================================================

# !!!!! VISAS DIENAS NODARBIBAS !!!!!
def main(request):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    return redirect ('day_list', d_id=4)


def day_list(request, d_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    dienas = [-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28] # DIENAS 0 --> SHODIENA
    datumi = []

    datums = today + datetime.timedelta( days=dienas[int(d_id)] ) # datums
    dienas_nodarb = Grafiks.objects.filter(sakums__startswith=datums).order_by('sakums') # datuma nodarbibas

    for d in range(0,33):
        datumi.append(today + datetime.timedelta( days=dienas[d] ))

    args['title'] = datums
    args['shodiena'] = datetime.date.today()
    args['data'] = dienas_nodarb
    args['datumi'] = datumi
    return render_to_response( 'day_data.html', args )

# !!!!! KONKRETA DIENAS NODARBIBA !!!!!
def nod_list(request, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')

    klienti = Grafiks.objects.get(id=g_id).nod.all()
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'day_kli_data.html', args )


# !!!!! NODARBIBAS ATEIKUMI !!!!!
def cancel_list(request, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')

    klienti = Grafiks.objects.get(id=g_id).ateikt.all()
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'day_cancel_data.html', args )

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
