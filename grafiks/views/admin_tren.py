# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from grafiks.models import Grafiks, Planotajs
from grafiks.forms import TrenRelForm

from nodarb.forms import TrenerisForm, TrenerisAvatarForm
from nodarb.models import *


from datetime import date as date_class # to test if end_date is entered using date class test
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
# !!!!! Treneru Aizvietošana sākot ar datumu !!!!!
def tren_aizv_plan( request, error=0 ):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['form'] = TrenRelForm

        args.update(csrf(request))      # ADD CSRF TOKEN
        if username.is_superuser:
            args['django'] = True
        args['admin'] = True
        args['max_date'] = today + datetime.timedelta(days=28+28)
        args['today'] = today

       # ERROR MODAL --> show
        if int(error) == 1: # Datums pagātnē
            args['error'] = True
            args['error_code_1'] = True
        if int(error) == 2: # Nekorekts datuma formāts
            args['error'] = True
            args['error_code_2'] = True
        if int(error) == 3: # Nav izvēlēts Treneris
            args['error'] = True
            args['error_code_3'] = True
        if int(error) == 4: # Nodarbība beigusies
            args['error'] = True
            args['error_code_4'] = True
        if int(error) == 5: # datums ievadīts pirms start_date
            args['error'] = True
            args['error_code_5'] = True


        days = []
        for i in range (0,7):
            day = Planotajs.objects.filter( diena=i ).order_by( 'laiks' )
            days.append(day)

        args['data'] = days

        if request.POST: # Edit Post Submited...
                # Planotajs Modal dati
                 p_id = int(request.POST.get('p_id', ''))

                 date_str = request.POST.get('date', '')
                 try:
                     date = datetime.datetime.strptime( date_str, '%d/%m/%Y').date()
                 except: # DATE FORMAT ERROR
                     return redirect('tren_aizv_plan', error=2 )

                 new_tren = request.POST.get('treneris', '')
                 if new_tren == '': # nav treneris ERROR
                     return redirect('tren_aizv_plan', error=3 )

                 after_month = (datetime.datetime.today() + datetime.timedelta(days=28+28)).date()

                 plan = Planotajs.objects.get(id=p_id)
                 treneris = Treneris.objects.get( id = int( new_tren ) )

                 if isinstance(plan.end_date, date_class) == True and plan.end_date < today: # Nodarbība beigusies
                     return redirect('tren_aizv_plan', error=4 )

                 if date < plan.start_date: # Datums ir pirms nodarbības sākuma
                     return redirect('tren_aizv_plan', error=5 )

                 if date < today or date > after_month: # Datums pagājis
                     return redirect('tren_aizv_plan', error=1 )

                 d = date
                 while d <= after_month:
                     if int(d.weekday()) == int(plan.diena):
                         temp_date = datetime.datetime.combine(d, datetime.datetime.min.time())	# Date to DateTime
                         new_sakums = temp_date.replace( hour = plan.laiks.hour, minute = plan.laiks.minute)

                         try:
                             temp_graf = Grafiks.objects.get(sakums = new_sakums, nodarbiba = plan.nodarbiba, telpa = plan.telpa)
                             temp_graf.treneris = treneris
                             temp_graf.save()
                         except:
                              pass
                     d += datetime.timedelta(days=1)

                 new_plan = Planotajs( diena = plan.diena, laiks = plan.laiks, ilgums = plan.ilgums, nodarbiba = plan.nodarbiba,
                                       treneris = treneris, telpa = plan.telpa, vietas = plan.vietas,
                                       start_date = date, end_date = plan.end_date )
                 new_plan.save()

                 plan.end_date = date - datetime.timedelta(days=1)
                 plan.save()
                # UPDATE Relations and Nodarbības redz
                 os.system('python /pieraksts/manage.py chk_rel')
                 os.system('python /pieraksts/manage.py chk_redz')
                 return redirect('tren_aizv_plan')

        return render_to_response ( 'tren_aizv_plan.html', args )
    return redirect('/reception/login/')

# =======================================================================================================

# !!!!! Treneru Kartiņa !!!!!
def treneri_edit(request):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['form'] = TrenerisForm  # add Nodarbibas form to args
        args['avatar_form'] = TrenerisAvatarForm

        args.update(csrf(request))      # ADD CSRF TOKEN
        if username.is_superuser:
            args['django'] = True
        args['admin'] = True

        args['treneri'] = Treneris.objects.all().order_by('vards')

        if request.POST:
            try:
                avatar_form = TrenerisAvatarForm( request.POST, request.FILES )
                if avatar_form.is_valid():
              #      t_id = request.POST.get('t_id', '') <-- NOT USED
                    t_slug = request.POST.get('t_slug', '')
                    t_vards = request.POST.get('t_vards', '')
                    t_apraksts = request.POST.get('t_apraksts', '')
                    t_avatar = avatar_form.cleaned_data['avatar']
                    args['print'] = t_avatar

                    tren_edit = Treneris.objects.get(slug=t_slug)

                    if t_avatar != '':
                        tren_edit.avatar = t_avatar

                    tren_edit.vards = t_vards
                    tren_edit.apraksts = t_apraksts
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
