# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from grafiks.models import Grafiks, Planotajs
from grafiks.forms import *

from main import mail

import datetime
today = datetime.date.today()

import os

# ========================================================================================================

# !!!!! ADMIN NODARBIBAS ATCELSHANA NEDELAS IZVELE !!!!!
def graf_list(request):
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
        return render_to_response ( 'del_graf.html', args )
    return redirect('/reception/login/')


# !!!!! ADMIN NODARBIBAS ATCELSHANA DIENAS IZVELE !!!!!
def week_list(request, w_id):
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
        return render_to_response ( 'del_graf.html', args )
    return redirect('/reception/login/')

# !!!!! ADMIN NODARBIBAS ATCELSHANA !!!!!
def graf_cancel(request, w_id, g_id):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        if username.is_superuser:
            args['django'] = True
        args['admin'] = True

        nod_atcelshana(g_id)	# nodarbības atcelšana

       # UPDATE Relations and Nodarbības redz
        os.system('python /pieraksts/manage.py chk_rel')
        os.system('python /pieraksts/manage.py chk_redz')
        return redirect ( 'nod_plan', w_id=w_id )
    return redirect('/reception/login/')


# ========================================================================================================
# !!!!! PLANOTĀJS IZŅEMT NODARBĪBU IZVĒLE !!!!!
def plan_list( request, error=0 ):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args.update(csrf(request))      # ADD CSRF TOKEN
        if username.is_superuser:
            args['django'] = True
        args['admin'] = True
        args['max_date'] = today + datetime.timedelta(days=28+28)

        days = []
        for i in range (0,7):
            day = Planotajs.objects.filter( diena=i ).order_by( 'laiks' )
            days.append(day)

        args['data'] = days
        if int(error) == 1: # datumspagājis modal --> show
            args['date_error1'] = True
        if int(error) == 2: # datums nav korekts modal --> show
            args['date_error2'] = True

        if request.POST: # Edit Post Submited...
            # Planotajs Modal dati
             p_id = int(request.POST.get('p_id', ''))
             diena = request.POST.get('diena', '')
             laiks_str = request.POST.get('laiks', '')
             laiks = datetime.datetime.strptime( laiks_str, '%H:%M')

             date_str = request.POST.get('date', '')
             try:
                 date = datetime.datetime.strptime( date_str, '%d/%m/%Y').date()
             except:
                 return redirect('plan_list', error = 2)

             if date < today: # Datums pagājis... ERROR
                 return redirect('plan_list', error = 1)

             else: # Datums - ok...
                 plan = Planotajs.objects.get(id=p_id)
                 plan.end_date = date
                 plan.save()

                 after_month = (datetime.datetime.today() + datetime.timedelta(days=28+28)).date()
                 if date <= after_month:
                     days_to_remove = []
                     d = date
# !!!!!! INSERT COUNTER --> TRIGER UPDATE Relations and Nodarbības redz
                     while d <= after_month: # veido masīvu no datumiem sākot ar izvēlēto, beidzot ar pēdējo pieraksta (ieskaitot)
                         if int(d.weekday()) == int(diena):
                             temp_date = datetime.datetime.combine(d, datetime.datetime.min.time())	# Date to DateTime
                             new_sakums = temp_date.replace(hour=laiks.hour, minute=laiks.minute)

                             try:
                                 temp_graf = Grafiks.objects.get(sakums = new_sakums, nodarbiba = plan.nodarbiba, treneris = plan.treneris)
                                 nod_atcelshana( temp_graf.id )
                             except:
                                 pass
                         d += datetime.timedelta(days=1)
                    # UPDATE Relations and Nodarbības redz
                     os.system('python /pieraksts/manage.py chk_rel')
                     os.system('python /pieraksts/manage.py chk_redz')
                 return redirect('plan_list')

        return render_to_response ( 'del_plan.html', args )
    return redirect('/reception/login/')


# ========================================================================================================
# !!!!! NODARBĪBAS PIERAKSTU ATCELŠANA UN E_MAIL NOTIFICATION !!!!!
def nod_atcelshana(g_id):
        nodarb = Grafiks.objects.get(id=g_id)
        klienti = nodarb.nod.all()
        for k in klienti:
            try: # reception Pieraksts may not include e-mail
#                pass
                mail.send_cancel(k.klients.e_pasts, nodarb.sakums, nodarb.nodarbiba.nos) #SEND CANCEL MAIL
            except:
                pass
        nodarb.delete()


