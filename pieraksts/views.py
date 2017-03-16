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

    args['form'] = KlientsForm

#    args['title'] = getattr(Grafiks.objects.get( id=g_id )) # grafika ieraksts
#    args['grafiks'] = Grafiks.objects.filter( nodarbiba=Nodarb_tips.objects.get( slug=g_id ), treneris=Treneris.objects.get( slug=t_id ) )

    args.update(csrf(request)) # ADD CSRF TOKEN

    if request.POST:
        new_name = request.POST.get('name', '')     # usermname <= get variable from Form (name="user"), if not leave blank
        new_email = request.POST.get('email', '')     # user_email <= get variable from Form (name="emial"), if not leave blank
        new_tel = request.POST.get('tel', '')

        args['name'] = new_name
        args['email'] = new_email
        args['tel'] = new_tel

        error = False
        clients = Klienti.objects.all()
        new = 0
        for c in clients:
            if (c.e_pasts == new_email and c.tel != new_tel) or (c.tel == new_tel and c.e_pasts != new_email):
                # EPASTS SAKRIT TELEFONS NE
                error = True
#                pass
#            if c.tel == new_tel and c.e_pasts != new_email:
               # EPASTS neSAKRIT TELEFONS SAKRIT
#                pass
            if c.tel == new_tel and c.e_pasts == new_email:
               # klients jau eksiste
                c.pieteikuma_reizes += 1
                c.pedejais_pieteikums = datetime.datetime.now()
                c.save()
                new += 1

        if error == True:
            args['error'] = True
            args['email_error'] = u'ERROR'
            return render_to_response( 'pieraksts.html', args )

        if new == 0:
               # Jauns klients
                new_client = Klienti(vards=new_name, e_pasts=new_email, tel=new_tel, pieteikuma_reizes=1)
                new_client.save()

      # nodarbibu vietas minus 1
        nodarbiba = Grafiks.objects.get( id=g_id )
        nodarbiba.vietas -= 1
        nodarbiba.save()

        return redirect('/')

    else:
        return render_to_response( 'pieraksts.html', args )

