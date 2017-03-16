# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.http.response import Http404	# ERRORR 404
from django.core.exceptions import ObjectDoesNotExist

from django.template.loader import get_template
from django.template import Context, RequestContext		# RequestContext <-- get user from request

from django.core.context_processors import csrf	# csrf token

from nodarb.models import *
from klienti.models import Klienti
from grafiks.models import Grafiks, Planotajs

from pieraksts.forms import KlientsForm
from pieraksts.models import *

import datetime
from datetime import date
today = date.today()


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
def any(request, n_id):
    args = {}

    args['title'] = getattr(Nodarb_tips.objects.get( slug=n_id ), 'nos') # Nodarb_tips nosaukums
    args['nodarb_slug'] = n_id

    args['grafiks'] = Grafiks.objects.filter( nodarbiba = Nodarb_tips.objects.get( slug=n_id ), sakums__gt=today ).order_by('sakums') # , sakums__startswith=today 
    return render_to_response( 'select.html', args )


# !!! SPECIFIC trainer !!!
def specific(request, n_id, t_id):
    args = {}

    args['title'] = getattr(Nodarb_tips.objects.get( slug=n_id ), 'nos') # Nodarb_tips nosaukums
    args['nodarb_slug'] = n_id

    args['grafiks'] = Grafiks.objects.filter( nodarbiba=Nodarb_tips.objects.get( slug=n_id ), treneris=Treneris.objects.get( slug=t_id ), sakums__gt=today ).order_by('sakums')
    return render_to_response( 'select.html', args )


# !!! Pieraksts !!!
def pieraksts(request, g_id):
    args = {}
    args['g_id'] = str(g_id)
    args['nodarb_slug'] = Grafiks.objects.get( id=g_id ).nodarbiba.slug
    args['title'] = Grafiks.objects.get( id=g_id ).nodarbiba.nos + '  | ' + Grafiks.objects.get( id=g_id ).treneris.vards
    args['laiks'] = Grafiks.objects.get( id=g_id ).sakums
    form = KlientsForm
    args['form'] = form
    args.update(csrf(request)) # ADD CSRF TOKEN

    if request.POST:
        form = KlientsForm( request.POST )
        if form.is_valid():
            new_name = form.cleaned_data['vards']
            new_email = form.cleaned_data['e_pasts']
            new_tel = form.cleaned_data['tel']

            error = False
            clients = Klienti.objects.all()
            new = 0
            for c in clients:
                if (c.e_pasts == new_email and c.tel != new_tel) or (c.tel == new_tel and c.e_pasts != new_email):
                   # EPASTS VAI TELEFONS JAU TIEK IZMANTOTS
                    error = True
                    args['error_msg'] = u' E-pasts vai Tālrunis jau ir reģistrēts citam klientam'

                if c.tel == new_tel and c.e_pasts == new_email and c.vards != new_name:
                   # CITS KLIENTA VARDS
                    error = True
                    args['error_msg'] = u' Cits klienta vārds'

                if c.tel == new_tel and c.e_pasts == new_email and c.vards == new_name:
                   # klients jau eksiste
                    if getattr(Grafiks.objects.get( id=g_id ), 'vietas') == 0: # IF VIETAS=0 --> ERROR
                        error = True
                        args['error_msg'] = u' Atvainojiet visas nodarbības vietas jau ir aizņemtas'
                    else: # VIETAS > 0 --> Pieraksts
                        c.pieteikuma_reizes += 1
                        c.pedejais_pieteikums = datetime.datetime.now()
                        c.save()
                        new += 1

                        nodarbiba = Grafiks.objects.get( id=g_id ) # VIETAS -1
                        nodarbiba.vietas -= 1
                        nodarbiba.save()

                        pieraksts = Pieraksti(klients=c, nodarbiba=nodarbiba) # PIETEIKUMS --> ACCEPT
                        pieraksts.save()
                      # Pieraksts sekmigs
                        args['msg'] = u'pieraksts sekmīgs'

            if new == 0:
           # Jauns klients
                if getattr(Grafiks.objects.get( id=g_id ), 'vietas') == 0: # IF VIETAS=0 --> ERROR
                    error = True
                    args['error_msg'] = u' Atvainojiet visas nodarbības vietas ir aizņemtas'
                else: # VIETAS > 0 --> Pieraksts
                    new_client = Klienti(vards=new_name, e_pasts=new_email, tel=new_tel, pieteikuma_reizes=1)
                    new_client.save()

                    nodarbiba = Grafiks.objects.get( id=g_id ) # VIETAS -1
                    nodarbiba.vietas -= 1
                    nodarbiba.save()

                    pieraksts = Pieraksti(klients=new_client, nodarbiba=nodarbiba) # PIETEIKUMS --> ACCEPT
                    pieraksts.save()
                    args['msg'] = u'pieraksts sekmīgs'
                  # Pieraksts sekmigs
                    return render_to_response( 'pieraksts.html', args )

            if error == True:
                args['error'] = True
                args['form'] = form     # ERROR MESSAGE
                return render_to_response( 'pieraksts.html', args )

        else:
            args['form'] = form	# ERROR MESSAGE
            return render_to_response( 'pieraksts.html', args )
    return render_to_response( 'pieraksts.html', args )


# !!!!! ATCELT !!!!!
def cancel(request, id):
    try:
        pieraksts = Pieraksti.objects.get( atteikuma_kods = id)
    except ObjectDoesNotExist:	# not existing --> 404
        raise Http404
    args = {}
    args['data'] = pieraksts
    args['id'] = id
    return render_to_response( 'cancel.html', args )


# !!!!! ATCELT-OK !!!!!
def cancel_ok(request, id):
    try:
        pieraksts = Pieraksti.objects.get( atteikuma_kods = id)
    except ObjectDoesNotExist:	# not existing bilde --> 404
        raise Http404
    args = {}
    args['data'] = pieraksts
# Grafiks.vietas +=1
    pieraksts.nodarbiba.vietas += 1
    pieraksts.nodarbiba.save()
# ADD Ateikumi
    atteikums = Atteikumi( klients=pieraksts.klients, nodarbiba=pieraksts.nodarbiba )
    atteikums.save()
# Klients.atteikumi -=1

# DELETE PIERAKSTS
    pieraksts.delete()

    return render_to_response( 'canceled.html', args )
