# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

from grafiks.models import Grafiks, Planotajs
from grafiks.forms import *

from nodarb.forms import Nodarb_tipsForm
from nodarb.models import Nodarb_tips


from datetime import date as date_class # to test if end_date is entered using date class test
import datetime
today = datetime.date.today()

import os

# ========================================================================================================

# !!!!! SUPERUSER PIEVIENOT GRAFIKAM JAUNU NODARBIBU !!!!!
def graf_add(request):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args.update(csrf(request))      # ADD CSRF TOKEN
        if username.is_superuser:
            args['django'] = True
        args['admin'] = True
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

                    if date <= after_month:	# jāieliek esošajā grafikā
                        if isinstance(end_date, date_class) == True and end_date < after_month: # ja end_date ir norādīts un ir maszāks par after_month
                            after_month = end_date

                        d = date
                        while d <= after_month: # iet pa datumiem sākot ar izvēlēto, beidzot ar pēdējo (ieskaitot) un veido Grafiks objektus
                            if int(d.weekday()) == int(diena):
                                temp_date = datetime.datetime.combine(d, datetime.datetime.min.time())	# Date to DateTime
                                new_sakums = temp_date.replace(hour=laiks.hour, minute=laiks.minute)

                               # Create Grafiks Object
                                new_graf = Grafiks(sakums = new_sakums, ilgums = ilgums, nodarbiba = nodarbiba, treneris = treneris, telpa = telpa, vietas = vietas)
                                new_graf.save()
                            d += datetime.timedelta(days=1)

                    if end_date != False: # INCLUDE END_DATE
                        new_plan = Planotajs(diena = diena, laiks = laiks, ilgums = ilgums, nodarbiba = nodarbiba, treneris = treneris, telpa = telpa, vietas = vietas, start_date = date, end_date = end_date)
                    else: # WITHOUT END_DATE
                        new_plan = Planotajs(diena = diena, laiks = laiks, ilgums = ilgums, nodarbiba = nodarbiba, treneris = treneris, telpa = telpa, vietas = vietas, start_date = date)

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
# !!!!! Nodarbību Kartiņa !!!!!
def nodarbibas_edit(request):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['form'] = Nodarb_tipsForm  # add Nodarbibas form to args

        args.update(csrf(request))      # ADD CSRF TOKEN
        if username.is_superuser:
            args['django'] = True
        args['admin'] = True

        args['nodarbibas'] = Nodarb_tips.objects.all().order_by('nos')

        if request.POST:
           # test POST for Nodarb_tips changes...
            try:
                n_id = request.POST.get('n_id', '')
                n_slug = request.POST.get('n_slug', '')
                n_nos = request.POST.get('n_nos', '')
                n_apraksts = request.POST.get('n_apraksts', '')

                nod_edit = Nodarb_tips.objects.get(slug=n_slug)
                nod_edit.nos = n_nos
                nod_edit.apraksts = n_apraksts
                nod_edit.save()
               # if no errors...
                return redirect ('nodarbibas')
            except:
                pass

           # Check ADD FORM...
            form = Nodarb_tipsForm( request.POST )
            if form.is_valid(): # create new Nodarb_tips...
                nod_new = Nodarb_tips(**form.cleaned_data)
                nod_new.save()
                return redirect ('nodarbibas')

            else: # Form not valid...
                args['form'] = form
                args['add_error'] = True

        return render_to_response ( 'nod_list.html', args )
    return redirect('/reception/login/')

