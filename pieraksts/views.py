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

# E-pasta modulis
from main import mail
from slugify import slugify

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

    t = trener_list(n_id)

    if not t:
        return redirect ('main') # Temporary solution ( Nodarbiba redz=True, no coresponding Grafiks entries)

    if len(t) > 1:
         return redirect( 'any', n_id=n_id) # ===> ANY TRAINER
    return redirect( 'specific', n_id=n_id, t_id=t[0].slug ) # ===> SPECIFIC TRAINER

# =================================================================================================================

# !!! ANY trainer !!!
def any(request, n_id):
    try:
        n = Nodarb_tips.objects.get( slug=n_id ) # Nodarbiba
    except ObjectDoesNotExist:  # not existing --> 404
        return redirect ('main')
    args = {}
    args['title'] = getattr( n, 'nos') + u' - Visi' # Nodarb_tips nosaukums
    args['nodarb_slug'] = n_id
    args['treneri'] = trener_list( n_id )

    grafiks_data = []
    start_time = datetime.datetime(today.year, today.month, today.day)
    end_time = today.replace(hour=23, minute=59, second=59)

    gr = Grafiks.objects.filter(nodarbiba = n, sakums__range=( datetime.datetime.now() , end_time)).order_by('sakums')
    if gr.count() != 0:
        grafiks_data.append(gr)

    for day in range(1,29):
        gr = Grafiks.objects.filter(nodarbiba = n, sakums__range=( start_time + datetime.timedelta( days=day) , end_time + datetime.timedelta( days=day ))).order_by('sakums')
        if gr.count() != 0:
            grafiks_data.append(gr)
    args['grafiks'] = grafiks_data

    if (len(grafiks_data) % 4) == 0:
        args['carousel_end'] = len(grafiks_data)

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
    args['title'] = getattr( n, 'nos') + ' - ' + getattr( t, 'vards') # Nodarb_tips nosaukums
    args['nodarb_slug'] = n_id
    args['treneri'] = trener_list( n_id )

    grafiks_data = []
    start_time = datetime.datetime(today.year, today.month, today.day)
    end_time = today.replace(hour=23, minute=59, second=59)

    gr = Grafiks.objects.filter(nodarbiba = n, treneris = t, sakums__range=( datetime.datetime.now() , end_time)).order_by('sakums')
    if gr.count() != 0:
        grafiks_data.append(gr)

    for day in range(1,29):
        gr = Grafiks.objects.filter(nodarbiba = n, treneris = t, sakums__range=( start_time + datetime.timedelta( days=day) , end_time + datetime.timedelta( days=day ))).order_by('sakums')
        if gr.count() != 0:
            grafiks_data.append(gr)
    args['grafiks'] = grafiks_data

    if (len(grafiks_data) % 4) == 0:
        args['carousel_end'] = len(grafiks_data)

    args['back'] = False
    return render_to_response( 'select.html', args )


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
           # SLUGIFY "Vārds Uzvārds" --> "vards_uzvards"
            new_name = slugify(form.cleaned_data['vards']).lower()
            new_email = form.cleaned_data['e_pasts'].lower()
            new_tel = form.cleaned_data['tel']
           # REMOVE +371 etc.
            if new_tel.startswith('+371 '):
                new_tel = new_tel[5:]
            elif new_tel.startswith('+371'):
                new_tel = new_tel[4:]
            else:
                pass


            args['vards'] = form.cleaned_data['vards']
            args['epasts'] = new_email
            args['telefons'] = form.cleaned_data['tel']

            error = False
            clients = Klienti.objects.all()
            new = 0
           # meklejam kljudas pieteikuma forma
            for c in clients:
                if c.e_pasts == new_email and c.vards != new_name:
                   # CITS KLIENTA VARDS
                    error = True
                    args['error_msg'] = u' Autorizācijas kļūda, nekorekts lietotāja vārds'

            if error == True:
                args['error'] = True
                args['form'] = form     # ERROR MESSAGE
                return render_to_response( 'pieraksts.html', args )

            for c in clients:
                if c.e_pasts == new_email and c.vards == new_name:
                   # klients jau eksiste
                    if getattr(Grafiks.objects.get( id=g_id ), 'vietas') < 1: # IF VIETAS=0 --> ERROR
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
                        pieraksts.save()
                        try:
                           mail.send_email(new_email, nod.nodarbiba.nos, nod.sakums, pieraksts.atteikuma_kods)
                        except:
                           pass
                 # Pieraksts sekmigs
                        args['back'] = False
                        return render_to_response( 'success.html', args )

            if error == True:
                args['error'] = True
                args['form'] = form     # ERROR MESSAGE
                return render_to_response( 'pieraksts.html', args )

            if new == 0:
           # Jauns klients
                if getattr(Grafiks.objects.get( id=g_id ), 'vietas') < 1: # IF VIETAS=0 --> ERROR
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
                    pieraksts.save()
                    try:
                      mail.send_email(new_email, nod.nodarbiba.nos, nod.sakums, pieraksts.atteikuma_kods)
                    except:
                      pass
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
    args.update(csrf(request)) # ADD CSRF TOKEN
    args['data'] = pieraksts

   # DISABLE CANCEL 3h before
    import pytz
    tz = pytz.timezone('EET')
    time_remain = ( pieraksts.nodarbiba.sakums - today.replace(tzinfo=tz) ).seconds / 3600
    if time_remain < 2:
        args['disable_cancel'] = True

    args['id'] = id
    return render_to_response( 'cancel.html', args )


# !!!!! ATCELT POST !!!!!
def cancel_ok(request):
    args = {}
    if request.POST:
        id = str(request.POST.get('cancel_id', ''))
        try:
            pieraksts = Pieraksti.objects.get( atteikuma_kods = id)
        except ObjectDoesNotExist:  # not existing code --> 404
            return redirect ('main')

        args['data'] = pieraksts
# Grafiks.vietas +=1
        pieraksts.nodarbiba.vietas += 1
        pieraksts.nodarbiba.save()
# ADD Ateikumi
        atteikums = Atteikumi( pieraksta_laiks=pieraksts.pieraksta_laiks, klients=pieraksts.klients, nodarbiba=pieraksts.nodarbiba )
        atteikums.save()
# Klients.atteikumi -=1
        pieraksts.klients.atteikuma_reizes +=1
        pieraksts.klients.save()
# DELETE PIERAKSTS
        pieraksts.delete()
    return render_to_response( 'canceled.html', args )


# !!!!! ATCELT GET !!!!!
def old_cancel_ok(request, id):
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
    atteikums = Atteikumi( pieraksta_laiks=pieraksts.pieraksta_laiks, klients=pieraksts.klients, nodarbiba=pieraksts.nodarbiba )
    atteikums.save()
# Klients.atteikumi -=1
    pieraksts.klients.atteikuma_reizes +=1
    pieraksts.klients.save()
# DELETE PIERAKSTS
    pieraksts.delete()
    return render_to_response( 'canceled.html', args )
