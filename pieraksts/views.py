# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.http.response import Http404	# ERRORR 404
from django.core.exceptions import ObjectDoesNotExist

from django.template.loader import get_template
from django.template import Context, RequestContext		# RequestContext <-- get user from request

from nodarb.models import *
from grafiks.models import Grafiks

# !!! Nodarbibas izvele !!!
def home(request):
    args = {}
    args['title'] = 'Nodarbības'
    args['nodarbibas'] = Nodarb_tips.objects.all() # visas nodarbibas
    return render_to_response( 'nodarb.html', args )


# !!! Trenera izvele !!!
def tren(request, n_id):
    args = {}
    treneri_rel = Nodarb_tips.objects.get( slug=n_id ).n.all() #nodarbiba(slug) ... n-relacija ... all() ... visi objekti
    treneri = []
    for t in treneri_rel:
       treneri.append(getattr( t, 'treneris') ) # relaciju objektu parametrs "Treneris"

    if len(treneri) > 1:
        args['any'] = True # ja vairaki tad "jebkursh brivais"

    args['title'] = getattr(Nodarb_tips.objects.get( slug=n_id ), 'nos') # Nodarb_tips nosaukums
    args['nodarb_slug'] = n_id
    args['treneri'] = treneri
    return render_to_response( 'treneri.html', args )


# !!! ANY trainer !!!
def any(request, n_id, t_id):
    args = {}
    return render_to_response( 'select.html', args )
