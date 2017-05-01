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

# !!!!! NODARBIBAS LAIKU OVERLAP CHEKER !!!!!
def nod_check(n_id, k_id):
    result = False	# denied Pieraksts
    n = Grafiks.objects.get( id=n_id )
    nod_start = getattr( n, 'sakums')
    nod_end = getattr( n, 'sakums') + datetime.timedelta(minutes=int(getattr( n, 'ilgums')))

    nod_date = nod_start.date()
    date_nod = Grafiks.objects.filter( sakums__startswith = nod_date ).order_by('sakums')

    count = 0
    for d in date_nod:
        end = d.sakums + datetime.timedelta(minutes=int(d.ilgums))
        Overlap = max(nod_start, d.sakums) < min(nod_end, end)
        if Overlap == True:
            try:
                pieraksti_nodarb = Pieraksti.objects.get( klients = k_id, nodarbiba = d )
                count += 1
            except Pieraksti.DoesNotExist:
                pass
            except:
                count += 1

    if count != 0:
        return False # Pieraksts --> DENIED
    else:
        return True


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
