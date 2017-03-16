# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.http.response import Http404	# ERRORR 404
from django.core.exceptions import ObjectDoesNotExist

from django.template.loader import get_template
from django.template import Context, RequestContext		# RequestContext <-- get user from request

#from django.contrib.auth.models import User	# autorisation library
#from django.contrib import auth			# autorisation library

from pieraksts.models import *
from grafiks.models import Grafiks

#import datetime
#import pytz

from datetime import date
today = date.today()

# !!!!! VISAS DIENAS NODARBIBAS !!!!!
def main(request):
    sodien = Grafiks.objects.filter(sakums__startswith=today).order_by('sakums')
    args = {}
    args['title'] = today
    args['data'] = sodien
    return render_to_response( 'day_data.html', args )


# !!!!! KONKRETA DIENAS NODARBIBA !!!!!
def nod_list(request, g_id):
    args = {}
    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')

    klienti = Grafiks.objects.get(id=g_id).nod.all()
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'kli_data.html', args )


# !!!!! NODARBIBAS ATEIKUMI !!!!!
def cancel_list(request, g_id):
    args = {}
    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')

    klienti = Grafiks.objects.get(id=g_id).ateikt.all()
    args['data'] = klienti
    args['g_id'] = g_id
    return render_to_response( 'cancel_data.html', args )

