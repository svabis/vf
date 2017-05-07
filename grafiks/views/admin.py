# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth			# autorisation library
from django.core.context_processors import csrf

from pieraksts.models import *
from grafiks.models import Grafiks, Planotajs
from grafiks.forms import PlanotajsForm
from nodarb.models import *

# Pieraksta statistikas modulis
from statistika import day_stat

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


# !!!!! SUPERUSER NODARBIBAS ATCELSHANA DIENAS IZVELE !!!!!
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

        args['w_id'] = w_id
        args['data'] = grafiks
        return render_to_response ( 'nod_plan.html', args )
    return redirect('/reception/login/')

# !!!!! SUPERUSER NODARBIBAS ATCELSHANA !!!!!
def graf_cancel(request, w_id, g_id):
    username = auth.get_user(request)
    if username.is_superuser:
        args = {}
        args['super'] = True

        nod_atcelshana(g_id)	# nodarbības atcelšana

        return redirect ( 'nod_plan', w_id=w_id )
    return redirect('/reception/login/')


def nod_atcelshana(g_id):
        nodarb = Grafiks.objects.get(id=g_id)
        klienti = nodarb.nod.all()
        for k in klienti:
            try: # reception Pieraksts may not include e-mail
                mail.send_cancel(k.klients.e_pasts, nodarb.sakums, nodarb.nodarbiba.nos) #SEND CANCEL MAIL

# !!!!! INSERT DELETE PIERAKSTS !!!!!

            except:
                pass
        nodarb.delete()


# ========================================================================================================

# !!!!! SUPERUSER PIEVIENOT GRAFIKAM JAUNU NODARBIBU !!!!!
def graf_add(request):
    username = auth.get_user(request)
    if username.is_superuser:
        args = {}
        args.update(csrf(request))      # ADD CSRF TOKEN
        args['super'] = True
        args['form'] = PlanotajsForm
        args['success'] = 'false'	# Modal never vaļā

        if request.POST:
            diena = request.POST.get('diena', '')
            laiks_str = request.POST.get('laiks', '')
            laiks = datetime.datetime.strptime( laiks_str[:5], '%H:%M')

            ilgums = int(request.POST.get('ilgums', ''))
            vietas = int(request.POST.get('vietas', ''))

            nodarbiba = Nodarb_tips.objects.get( id = int(request.POST.get('nodarbiba', '')) )
            treneris = Treneris.objects.get( id = int(request.POST.get('treneris', '')) )
            telpa = Telpa.objects.get( id = int(request.POST.get('telpa', '')) )

            chk_once = request.POST.get('chk', '')
            date_str = request.POST.get('date', '')
            date = datetime.datetime.strptime( date_str, '%d/%m/%Y').date()

            after_month = (datetime.datetime.today() + datetime.timedelta(days=28)).date()

            if chk_once == "on":	# ja nodarbiba notiks vienu reizi -->
                temp_date = datetime.datetime.combine(date, datetime.datetime.min.time())	# Date to DateTime
                new_sakums = temp_date.replace(hour=laiks.hour, minute=laiks.minute)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!! INSERT Nodarbība veidota vēsturē ERROR !!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!! INSERT Nodarbība OVELAP ERROR !!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                new_graf = Grafiks(sakums=new_sakums, ilgums=ilgums, nodarbiba=nodarbiba, treneris=treneris, telpa=telpa, vietas=vietas)
                new_graf.save()
                args['nodarbiba'] = new_graf	# pievienota viena nodarbība --> Modal_success
                args['one'] = True	# Modal_success --> viena apraksts

            else:	# ja atkārtojās, tad  veidojam Planotāja ierakstu
                if date <= after_month:	# jāieliek esošajā grafikā

# !!!!!!!! WEEKDAY NO DIENA... FOR DATE TO AFTER_MONTH... INSERT GRAFIKS
#                    args['message'] = u'datumi iekļaujās'
                    pass

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!! INSERT Nodarbība OVELAP ERROR !!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

                new_plan = Planotajs(diena=diena, laiks=laiks, ilgums=ilgums, nodarbiba=nodarbiba, treneris=treneris, telpa=telpa, vietas=vietas, start_date=date)
                args['nodarbiba'] = new_plan	# pievienots grafikam -->

                new_plan.save()
            args['success'] = 'true'	# atverās modal ar "Pievienots sekmīgi"

# !!! ERRORS CITUR !!!
#            args['error'] = u' KĻŪDA'
            args['message'] = u' Nodarbība pievienota sekmīgi'

        return render_to_response('add_plan.html', args)
    return redirect('/reception/login/')

# =======================================================================================================

# !!!!! TRENERU AIZVIETOSANA NEDELAS IZVELE !!!!!
def tren_list( request ):
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
        return render_to_response ( 'tren_aizv.html', args )
    return redirect('/reception/login/')

def tren_week_list( request, w_id ):
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

        args['w_id'] = w_id
        args['data'] = grafiks
        return render_to_response ( 'tren_aizv.html', args )
    return redirect('/reception/login/')

def tren_aizv( request, w_id, g_id ):
    return True


