# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from pieraksts.models import *
from grafiks.models import Grafiks, Planotajs
from grafiks.forms import *
from nodarb.models import *

from main import mail

import datetime
import pytz
today = datetime.date.today()
tz = pytz.timezone('UTC')

import os

def kalend(request):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['super'] = True
        args['today'] = today
#        weeks = []
#        weeks.append(today)

#        next = today + datetime.timedelta( days=7 - int( today.weekday()) ) # next week monday
#        for _ in range (0,8): # add 4 weeks in row
#            weeks.append(next)
#            next = next + datetime.timedelta(days=7)

#        args['week'] = weeks
        return render_to_response ( 'kalend.html', args )
    return redirect('/reception/login/')


# ========================================================================================================

# !!!!! SUPERUSER NODARBIBAS ATCELSHANA NEDELAS IZVELE !!!!!
def graf_list(request):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['super'] = True
        weeks = []
        weeks.append(today)

        next = today + datetime.timedelta( days=7 - int( today.weekday()) ) # next week monday
        for _ in range (0,8): # add 4 weeks in row
            weeks.append(next)
            next = next + datetime.timedelta(days=7)

        args['week'] = weeks
        return render_to_response ( 'nod_plan.html', args )
    return redirect('/reception/login/')


# !!!!! SUPERUSER NODARBIBAS ATCELSHANA DIENAS IZVELE !!!!!
def week_list(request, w_id):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['super'] = True
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
        return render_to_response ( 'nod_plan.html', args )
    return redirect('/reception/login/')

# !!!!! SUPERUSER NODARBIBAS ATCELSHANA !!!!!
def graf_cancel(request, w_id, g_id):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['super'] = True

        nod_atcelshana(g_id)	# nodarbības atcelšana

       # UPDATE Relations and Nodarbības redz
#        os.system('python /pieraksts/manage.py chk_rel')
#        os.system('python /pieraksts/manage.py chk_redz')
        return redirect ( 'nod_plan', w_id=w_id )
    return redirect('/reception/login/')


def nod_atcelshana(g_id):
        nodarb = Grafiks.objects.get(id=g_id)
        klienti = nodarb.nod.all()
        for k in klienti:
            try: # reception Pieraksts may not include e-mail
                pass
#                mail.send_cancel(k.klients.e_pasts, nodarb.sakums, nodarb.nodarbiba.nos) #SEND CANCEL MAIL
            except:
                pass
        nodarb.delete()


# ========================================================================================================

# !!!!! SUPERUSER PIEVIENOT GRAFIKAM JAUNU NODARBIBU !!!!!
def graf_add(request):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args.update(csrf(request))      # ADD CSRF TOKEN
        args['super'] = True
        args['form'] = PlanotajsForm
        args['success'] = 'false'	# Modal never vaļā

        if request.POST:
            form = PlanotajsForm( request.POST )

            if form.is_valid(): # and form2.is_valid():
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
                end_date_str = request.POST.get('end_date', '')

                date = datetime.datetime.strptime( date_str, '%d/%m/%Y').date()
                if end_date_str != "":
                    end_date = datetime.datetime.strptime( end_date_str, '%d/%m/%Y').date()
                else:
                    end_date = False

                after_month = (datetime.datetime.today() + datetime.timedelta(days=28+28)).date()

                if chk_once == "on":	# ja nodarbiba notiks vienu reizi -->
                    temp_date = datetime.datetime.combine(date, datetime.datetime.min.time())	# Date to DateTime
                    new_sakums = temp_date.replace(hour=laiks.hour, minute=laiks.minute)

                   # !!!!!!! CHECK Nodarbība veidota vēsturē OR nākotnē --> ERROR !!!!!!!!
                    if new_sakums < datetime.datetime.now():
                        args['form'] = form
                        args['error'] = u' Izvēlētais datums ir jau pagājis !!!'
                        return render_to_response('add_plan.html', args)
                    if new_sakums > (datetime.datetime.now() + datetime.timedelta(days=28+28)):
                        args['form'] = form
                        args['error'] = u' Izvēlētais datums ir ārpus Pieraksta sistēmas - vairāk kā 2 mēneši uz priekšu !!!'
                        return render_to_response('add_plan.html', args)
                    else:

                   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                   # !!!!!!! INSERT Nodarbība OVELAP ERROR !!!!!!!!
                   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!
                        new_graf = Grafiks(sakums=new_sakums, ilgums=ilgums, nodarbiba=nodarbiba, treneris=treneris, telpa=telpa, vietas=vietas)
                        new_graf.save()
                        args['nodarbiba'] = new_graf	# pievienota viena nodarbība --> Modal_success
                        args['one'] = True	# Modal_success --> viena apraksts
                        args['success'] = 'true'	# atverās modal ar "Pievienots sekmīgi"

                       # UPDATE Relations and Nodarbības redz
#                        os.system('python /pieraksts/manage.py chk_rel')
#                        os.system('python /pieraksts/manage.py chk_redz')
                        return render_to_response('add_plan.html', args)

                else:	# ja atkārtojās, tad  veidojam Planotāja ierakstu

                   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                   # !!!!!!! INSERT Nodarbība OVELAP ERROR !!!!!!!!
                   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!
                    if date <= after_month:	# jāieliek esošajā grafikā
                        days_to_add = []
                        d = date
                        while d <= after_month: # veido masīvu no datumiem sākot ar izvēlēto, beidzot ar pēdējo pieraksta (ieskaitot)
                            if int(d.weekday()) == int(diena):
                                temp_date = datetime.datetime.combine(d, datetime.datetime.min.time())	# Date to DateTime
                                new_sakums = temp_date.replace(hour=laiks.hour, minute=laiks.minute)

                                new_graf = Grafiks(sakums = new_sakums,
                                                   ilgums = ilgums,
                                                   nodarbiba = nodarbiba,
                                                   treneris = treneris,
                                                   telpa = telpa,
                                                   vietas = vietas) 	# Create Grafiks Object
                                new_graf.save()
                            d += datetime.timedelta(days=1)

                    if end_date != False: # INCLUDE END_DATE
                        new_plan = Planotajs(diena = diena,
                                         laiks = laiks,
                                         ilgums = ilgums,
                                         nodarbiba = nodarbiba,
                                         treneris = treneris,
                                         telpa = telpa,
                                         vietas = vietas,
                                         start_date = date,
                                         end_date = end_date)
                    else: # WITHOUT END_DATE
                        new_plan = Planotajs(diena = diena,
                                         laiks = laiks,
                                         ilgums = ilgums,
                                         nodarbiba = nodarbiba,
                                         treneris = treneris,
                                         telpa = telpa,
                                         vietas = vietas,
                                         start_date = date)

                    new_plan.save()
                    args['nodarbiba'] = new_plan	# pievienots grafikam -->
                    args['success'] = 'true'	# atverās modal ar "Pievienots sekmīgi" Plānotājam

                   # UPDATE Relations and Nodarbības redz
#                    os.system('python /pieraksts/manage.py chk_rel')
#                    os.system('python /pieraksts/manage.py chk_redz')
                    return render_to_response('add_plan.html', args)

            else: # form is not valid
                args['form'] = form
        return render_to_response('add_plan.html', args)
    return redirect('/reception/login/')

# =======================================================================================================

# !!!!! TRENERU AIZVIETOSANA NEDELAS IZVELE !!!!!
def tren_list( request ):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['super'] = True
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
        args.update(csrf(request))      # ADD CSRF TOKEN
        args['super'] = True
        args['form'] = TrenRelForm
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
        args['super'] = True

        if request.POST:
            new_tren = request.POST.get('treneris', '')
            if new_tren != '':
                treneris = Treneris.objects.get( id = int( new_tren ) )
                change = Grafiks.objects.get( id=g_id )
                change.treneris = treneris
                change.save()

        # UPDATE Relations and Nodarbības redz
#        os.system('python /pieraksts/manage.py chk_rel')
#        os.system('python /pieraksts/manage.py chk_redz')
        return redirect ( 'tren_week_list', w_id=w_id )
    return redirect('/reception/login/')


# =======================================================================================================

# !!!!! PLANOTĀJS IZNEMT NODARBIBU IZVELE !!!!!
def plan_list( request ):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args.update(csrf(request))      # ADD CSRF TOKEN
        args['super'] = True
        args['max_date'] = today + datetime.timedelta(days=28+28)

        if request.POST: # Edit Post Submited...
            # Planotajs Modal dati
             p_id = int(request.POST.get('p_id', ''))
             date_str = request.POST.get('date', '')
             date = datetime.datetime.strptime( date_str, '%d/%m/%Y').date()

             if date < today: # Datums pagājis... ERROR
                 args['date_error'] = True
             else: # Datums - ok...
                 plan = Planotajs.objects.get(id=p_id)
                 plan.end_date = date
                 plan.save()
# remove Grafiks objects...
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! INSERT BRAIN HERE !!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        days = []
        for i in range (0,7):
            day = Planotajs.objects.filter( diena=i ).order_by( 'laiks' )
            days.append(day)

        args['data'] = days

       # UPDATE Relations and Nodarbības redz
#        os.system('python /pieraksts/manage.py chk_rel')
#        os.system('python /pieraksts/manage.py chk_redz')
        return render_to_response ( 'del_plan.html', args )
    return redirect('/reception/login/')
