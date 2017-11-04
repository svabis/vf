# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from grafiks.models import Grafiks
from grafiks.forms import TrenRelForm

from nodarb.forms import TrenerisForm
from nodarb.models import *


import datetime
today = datetime.date.today()

import os

# =======================================================================================================

# !!!!! TRENERU AIZVIETOSANA NEDELAS IZVELE !!!!!
def tren_list( request ):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        if username.is_superuser:
            args['django'] = True
        args['admin'] = True
        weeks = []
        weeks.append(today)

        next = today + datetime.timedelta( days=7 - int( today.weekday()) ) # next week monday
        for _ in range (0,8): # add 4 weeks in row
            weeks.append(next)
            next = next + datetime.timedelta(days=7)

        args['week'] = weeks
        return render_to_response ( 'tren_aizv.html', args )
    return redirect('/reception/login/')

# !!!!! TRENERU AIZVIETOSANA NEDELAS SKATS !!!!!
def tren_week_list( request, w_id ):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['form'] = TrenRelForm

        args.update(csrf(request))      # ADD CSRF TOKEN
        if username.is_superuser:
            args['django'] = True
        args['admin'] = True

        weeks = []
        weeks.append(today)
        next = today + datetime.timedelta( days=7 - int( today.weekday()) ) # next week monday
        for _ in range (0,8): # add 4 weeks in row
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

        args['w_id'] = w_id # this week number
        if int(w_id) > 0: # previous week number
             args['pw_id'] = int(w_id) - 1
        if int(w_id) < 8: # next week number
             args['nw_id'] = int(w_id) + 1


        args['data'] = grafiks
        return render_to_response ( 'tren_aizv.html', args )
    return redirect('/reception/login/')


# !!!!! TRENERU AIZVIETOSANAS POST FORMA !!!!!
def tren_aizv( request, w_id, g_id ):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args.update(csrf(request))      # ADD CSRF TOKEN
        if username.is_superuser:
            args['django'] = True
        args['super'] = True

        if request.POST:
            new_tren = request.POST.get('treneris', '')
            if new_tren != '':
                treneris = Treneris.objects.get( id = int( new_tren ) )
                change = Grafiks.objects.get( id=g_id )
                change.treneris = treneris
                change.save()

                after_month = (datetime.datetime.today() + datetime.timedelta(days=28)).date()
                if change.sakums.date() <= after_month:
                   # UPDATE Relations and Nodarbības redz
                    os.system('python /pieraksts/manage.py chk_rel')
                    os.system('python /pieraksts/manage.py chk_redz')
        return redirect ( 'tren_week_list', w_id=w_id )
    return redirect('/reception/login/')


# =======================================================================================================

# !!!!! Treneru Kartiņa !!!!!
def treneri_edit(request):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['form'] = TrenerisForm  # add Nodarbibas form to args

        args.update(csrf(request))      # ADD CSRF TOKEN
        if username.is_superuser:
            args['django'] = True
        args['admin'] = True

        args['treneri'] = Treneris.objects.all().order_by('vards')

        if request.POST:
           # test POST for Nodarb_tips changes...
            try:
#                t_id = request.POST.get('t_id', '')
                t_slug = request.POST.get('t_slug', '')
                t_vards = request.POST.get('t_vards', '')
                t_apraksts = request.POST.get('t_apraksts', '')

                tren_edit = Treneris.objects.get(slug=t_slug)
                tren_edit.vards = t_vards
                tren_edit.apraksts = t_apraksts
# !!!!! tren_edit.avatar !!!!!
                tren_edit.save()
               # if no errors...
                return redirect ('treneri')
            except:
                pass

           # Check ADD FORM...
            form = TrenerisForm( request.POST, request.FILES )
            if form.is_valid(): # create new Nodarb_tips...
                tren_new = Treneris(**form.cleaned_data)
                tren_new.save()
                return redirect ('treneri')

            else: # Form not valid...
                args['form'] = form
                args['add_error'] = True

        return render_to_response ( 'tren_list.html', args )
    return redirect('/reception/login/')
