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

from main import mail

import datetime
today = datetime.datetime.now() # sakot no --> shodiena + pulkstens (tagad)

# !!!!! TRENERU LIST !!!!!
def trener_list( n_id ):
    nod = Nodarb_tips.objects.get( slug=n_id ) # Nodarbiba
    treneri_rel = nod.n.all() #nodarbiba(slug) ... n-relacija ... all() ... visi objekti
    treneri = []

    if treneri_rel.count() > 1:
       treneri.append('any')
    for t in treneri_rel:
       treneri.append(getattr( t, 'treneris') ) # relaciju objektu parametrs "Treneris"
    return treneri

# !!!!! NODARBIBAS LAIKU OVERLAP CHEKER !!!!!
def nod_check(n_id, k_id):
# ritina cauri Klients.Pieraksti
# katram njem [start, start + timedelta(min=nodarb.ilgums)]

# 1. parbauda vai jau nav pieraksts uz sho --> False
# 2. parbauda vai n_id.start ieklaujas laika kadam --> False
# 3. parbauda vai (n_id.start + timedelta(min=nodarb.ilgums) ieklaujas --> False
# 4. n_id sakas pirms un beidzas pec parbaudama --> False

# ELSE --> True

    if False:
        return False
    return True

# =================================================================================================================

# !!! Visas nodarbibas !!!
def home(request):
    args = {}
    args['title'] = 'Nodarbības'
    args['nodarbibas'] = Nodarb_tips.objects.filter( redz = True ).order_by('nos') # Atlasa redzamas nodarbibas
    return render_to_response( 'nodarb.html', args )

# !!! Nodarbibas izvele !!!
def tren(request, n_id):
    try:
        nod = Nodarb_tips.objects.get( slug=n_id ) # Nodarbiba
    except ObjectDoesNotExist:  # not existing --> 404
        return redirect ('main')

    if len(trener_list( n_id )) > 1:
         return redirect( 'any', n_id=n_id) # ===> ANY TRAINER
    return redirect( 'specific', n_id=n_id, t_id=trener_list(n_id)[0].slug ) # ===> SPECIFIC TRAINER

# =================================================================================================================

# !!! ANY trainer !!!
def any(request, n_id):
    try:
        n = Nodarb_tips.objects.get( slug=n_id ) # Nodarbiba
    except ObjectDoesNotExist:  # not existing --> 404
        return redirect ('main')
    args = {}
    args['title'] = getattr( n, 'nos') # Nodarb_tips nosaukums
    args['nodarb_slug'] = n_id
    args['treneri'] = trener_list( n_id )
    args['grafiks'] = Grafiks.objects.filter( nodarbiba = n, sakums__gt = today ).order_by('sakums')
    args['back'] = False
    return render_to_response( 'select.html', args )

# !!! SPECIFIC trainer !!!
def specific(request, n_id, t_id):
    try:
        n = Nodarb_tips.objects.get( slug=n_id ) # Nodarbiba
        t = Treneris.objects.get( slug=t_id ) # Treneris
    except ObjectDoesNotExist:  # not existing --> 404
        return redirect ('main')
    args = {}
    args['title'] = getattr( n, 'nos') # Nodarb_tips nosaukums
    args['nodarb_slug'] = n_id
    args['treneri'] = trener_list( n_id )
    args['grafiks'] = Grafiks.objects.filter( nodarbiba = n, treneris = t, sakums__gt = today ).order_by('sakums')
    args['back'] = False
    return render_to_response( 'select.html', args )

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!      INSERT BRAIN HERE       !!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# =================================================================================================================

# !!! Pieraksts !!!
def pieraksts(request, g_id):
    try:
        nod = Grafiks.objects.get( id=g_id )
    except ObjectDoesNotExist:  # not existing --> 404
        return redirect ('main')

    form = KlientsForm

    args = {}
    args['g_id'] = str(g_id)
    args['nodarb_slug'] = nod.nodarbiba.slug
    args['title'] = nod.nodarbiba.nos + ' - ' + nod.treneris.vards
    args['laiks'] = nod.sakums
    args['form'] = form
    args['back'] = True
    args['time'] =True
    args.update(csrf(request)) # ADD CSRF TOKEN

    if request.POST:
        form = KlientsForm( request.POST )
        if form.is_valid():
            new_name = form.cleaned_data['vards']
            new_email = form.cleaned_data['e_pasts']
            new_tel = form.cleaned_data['tel']
            args['vards'] = new_name
            args['epasts'] = new_email
            args['telefons'] = new_tel

            error = False
            clients = Klienti.objects.all()
            new = 0
           # meklejam kljudas pieteikuma forma
            for c in clients:
                if c.e_pasts == new_email and c.vards != new_name:
                   # CITS KLIENTA VARDS
                    error = True
                    args['error_msg'] = u' Cits klienta vārds'

            if error == True:
                args['error'] = True
                args['form'] = form     # ERROR MESSAGE
                return render_to_response( 'pieraksts.html', args )

            for c in clients:
                if c.e_pasts == new_email and c.vards == new_name:
                   # klients jau eksiste
                    if getattr(Grafiks.objects.get( id=g_id ), 'vietas') == 0: # IF VIETAS=0 --> ERROR
                        error = True
                        args['error_msg'] = u' Atvainojiet visas nodarbības vietas jau ir aizņemtas'
                    if nod_check(g_id, c) == False: # False --> jau ir pieraksts uz sho laiku
                        error = True
                        args['error_msg'] = u' Jūs uz šo laiku jau esat pierakstījies'
                    if error == False: # VIETAS > 0, PIERAKSTI NEPARKLAJAS --> Pieraksts
                        c.pieteikuma_reizes += 1
                        c.pedejais_pieteikums = datetime.datetime.now()
                        c.tel = new_tel # UPDATE tel nr ierakstu
                        c.save()
                        new += 1

                        nodarbiba = Grafiks.objects.get( id=g_id ) # VIETAS -1
                        nodarbiba.vietas -= 1
                        nodarbiba.save()

                        pieraksts = Pieraksti(klients=c, nodarbiba=nodarbiba) # PIETEIKUMS --> ACCEPT
                 # SEND ACCEPT MAIL WITH CANCEL CODE
                        mail.send_email(new_email, nod.nodarbiba.nos, nod.sakums, pieraksts.atteikuma_kods)
                        pieraksts.save()
                 # Pieraksts sekmigs
                        args['back'] = False
                        return render_to_response( 'success.html', args )

            if error == True:
                args['error'] = True
                args['form'] = form     # ERROR MESSAGE
                return render_to_response( 'pieraksts.html', args )

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
             # SEND ACCEPT MAIL WITH CANCEL CODE
                    mail.send_email(new_email, nod.nodarbiba.nos, nod.sakums, pieraksts.atteikuma_kods)
                    pieraksts.save()
             # Pieraksts sekmigs
                    args['back'] = False
                    return render_to_response( 'success.html', args )

            if error == True:
                args['error'] = True
                args['form'] = form     # ERROR MESSAGE
                return render_to_response( 'pieraksts.html', args )

        else:
            args['form'] = form	# ERROR MESSAGE
            return render_to_response( 'pieraksts.html', args )
    return render_to_response( 'pieraksts.html', args )

# =================================================================================================================

# !!!!! ATCELT !!!!!
def cancel(request, id):
    try:
        pieraksts = Pieraksti.objects.get( atteikuma_kods = id)
    except ObjectDoesNotExist:	# not existing code --> 404
        return redirect ('main')
    args = {}
    args['data'] = pieraksts
    args['id'] = id
    return render_to_response( 'cancel.html', args )


# !!!!! ATCELT-OK !!!!!
def cancel_ok(request, id):
    try:
        pieraksts = Pieraksti.objects.get( atteikuma_kods = id)
    except ObjectDoesNotExist:	# not existing code --> 404
        return redirect ('main')
    args = {}
    args['data'] = pieraksts
# Grafiks.vietas +=1
    pieraksts.nodarbiba.vietas += 1
    pieraksts.nodarbiba.save()
# ADD Ateikumi
    atteikums = Atteikumi( klients=pieraksts.klients, nodarbiba=pieraksts.nodarbiba )
    atteikums.save()
# Klients.atteikumi -=1
    pieraksts.klients.atteikuma_reizes +=1
    pieraksts.klients.save()
# DELETE PIERAKSTS
    pieraksts.delete()
    return render_to_response( 'canceled.html', args )
