# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth			# autorisation library
from django.core.context_processors import csrf

from pieraksts.models import *
from grafiks.models import Grafiks

from pieraksts.forms import KlientsReceptionForm

# Pieraksta statistikas modulis
from statistika import day_stat

from slugify import slugify

import datetime
import pytz
today = datetime.date.today()
tz = pytz.timezone('UTC')

# ========================================================================================================

# !!!!! NODARBIBAS LAIKU OVERLAP CHEKER !!!!!
def nod_check(n_id, k_id):
    result = False      # denied Pieraksts
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

# ========================================================================================================

# !!!!! VISAS DIENAS NODARBIBAS !!!!!
def main(request):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    return redirect ('day_list', d_id=0)


# !!!!! KONKRETA DIENA !!!!!
def day_list(request, d_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    dienas = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28] # DIENAS 0 --> SHODIENA
    datumi = []

    datums = today + datetime.timedelta( days=dienas[int(d_id)] ) # datums
    dienas_nodarb = Grafiks.objects.filter(sakums__startswith=datums).order_by('sakums') # datuma nodarbibas

    for d in range(0,29):
        datumi.append([(today + datetime.timedelta(days=dienas[d])), ((today + datetime.timedelta(days=dienas[d])).weekday())])

    args['title'] = datums
    args['shodiena'] = datetime.date.today()
    args['data'] = dienas_nodarb
    args['datumi'] = datumi
    args['d_id'] = d_id
    return render_to_response( 'day_data.html', args )

# !!!!! KONKRETA NODARBIBAS PIERAKSTI !!!!!
def nod_list(request, d_id, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')

    klienti = Grafiks.objects.get(id=g_id).nod.all()
    args['data'] = klienti
    args['g_id'] = g_id
    args['d_id'] = d_id

    args['datums'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums').date()
    args['shodiena'] = datetime.datetime.now().date()
    return render_to_response( 'day_kli_data.html', args )


# !!!!! KONKRETAS NODARBIBAS ATEIKUMI !!!!!
def cancel_list(request, d_id, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    args['title'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')

    klienti = Grafiks.objects.get(id=g_id).ateikt.all()
    args['data'] = klienti
    args['g_id'] = g_id
    args['d_id'] = d_id
    return render_to_response( 'day_cancel_data.html', args )

# ===================================================

# !!!!! KONKRETA DIENAS NODARBIBAS PRINT !!!!!
def print_nod(request, d_id, g_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True

    args['title'] = datetime.datetime.now()
    args['title2'] = getattr(Grafiks.objects.get( id=g_id ), 'nodarbiba')
    args['subtitle'] = getattr(Grafiks.objects.get( id=g_id ), 'sakums')
    args['treneris'] = getattr(Grafiks.objects.get( id=g_id ), 'treneris')

    klienti = Grafiks.objects.get(id=g_id).nod.all()
    args['data'] = klienti
    return render_to_response( 'day_kli_print.html', args )

# ===================================================

# !!!!! RECEPTION CANCEL !!!!!
def reception_cancel(request, d_id, g_id, p_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")

    try:
        pieraksts = Pieraksti.objects.get(id=p_id)
# ADD VIETAS uznodarbību
        pieraksts.nodarbiba.vietas += 1
        pieraksts.nodarbiba.save()
# Create Atteikums object
        atteikums = Atteikumi( pieraksta_laiks=pieraksts.pieraksta_laiks, klients=pieraksts.klients, nodarbiba=pieraksts.nodarbiba )
        atteikums.save()
# Klients.atteikumi -=1
        pieraksts.klients.atteikuma_reizes +=1
        pieraksts.klients.save()
# DELETE PIERAKSTS
        pieraksts.delete()
    except:
        pass
    return redirect( 'nod_list', d_id=d_id, g_id=g_id )

# ===================================================

# !!!!! RECEPTION PIERAKSTS !!!!!
def reception_pieraksts(request, d_id, n_id):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/reception/login/")
    try:
        nod = Grafiks.objects.get( id=n_id )
    except ObjectDoesNotExist:  # not existing --> 404
        return redirect ('day_list', d_id=d_id)
    args = {}
    if auth.get_user(request).is_superuser: # superuser --> Left menu available
        args['super'] = True
        super = True
    else:
        super = False

    form = KlientsReceptionForm

    args['d_id'] = d_id
    args['n_id'] = n_id
    args['title'] = nod.nodarbiba.nos + ' - ' + nod.treneris.vards
    args['subtitle'] = getattr(Grafiks.objects.get( id=n_id ), 'sakums')
    args['form'] = form
    args.update(csrf(request)) # ADD CSRF TOKEN

    if request.POST:
        form = KlientsReceptionForm( request.POST )
        if form.is_valid():
           # SLUGIFY "Vārds Uzvārds" --> "vards_uzvards"
            new_name = slugify(form.cleaned_data['vards']).lower()
            new_email = form.cleaned_data['e_pasts'].lower()
            new_tel = str(form.cleaned_data['tel'])
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
            new = 0 # jaunas lietotāja counters
            tel_err_count = 0 #telefona dublikātu counters

           # meklejam kljudas pieteikuma forma
            for c in clients:
                if c.tel == new_tel:
                    tel_err_count += 1
            if tel_err_count > 1:
                args['tel_msg'] = True
                args['form'] = form     # ERROR MESSAGE
                return render_to_response( 'rec_pierakst.html', args )

#            for c in clients:
#                if c.tel == new_tel and c.vards != new_name:
                   # CITS KLIENTA VARDS
#                    error = True
#                    args['error_msg'] = u' Autorizācijas kļūda, klienta tālrunim atbilst cits klients'

#            if error == True:
#                args['error'] = True
#                args['form'] = form     # ERROR MESSAGE
#                return render_to_response( 'rec_pierakst.html', args )

            for c in clients:
                if c.tel == new_tel and c.vards == new_name:
                   # klients jau eksiste
                    if getattr(Grafiks.objects.get( id=n_id ), 'vietas') < 1 and super != True: # IF VIETAS=0 --> ERROR
                        error = True
                        args['error_msg'] = u' Atvainojiet visas nodarbības vietas jau ir aizņemtas'

                    if nod_check(n_id, c) == False: # False --> jau ir pieraksts uz sho laiku
                        error = True
                        args['error_msg'] = u' Uz šo laiku klients jau ir pierakstījies'
                    if error == False: # VIETAS > 0, PIERAKSTI NEPARKLAJAS --> Pieraksts
                        c.pieteikuma_reizes += 1
                        c.pedejais_pieteikums = datetime.datetime.now()
#                        c.tel = new_tel # UPDATE tel nr ierakstu
                        c.save()
                        new += 1

                        nodarbiba = Grafiks.objects.get( id=n_id ) # VIETAS -1
                        if nodarbiba.vietas > 0:
                            nodarbiba.vietas -= 1
                        nodarbiba.save()

                        pieraksts = Pieraksti(klients=c, nodarbiba=nodarbiba) # PIETEIKUMS --> ACCEPT
                        pieraksts.save()
                 # Pieraksts sekmigs
                        day_stat.day_stat()
                        args['vards'] = form.cleaned_data['vards']
                        args['epasts'] = c.e_pasts
                        args['telefons'] = form.cleaned_data['tel']
                        return render_to_response ('rec_pier_success.html', args )

            if error == True:
                args['error'] = True
                args['form'] = form     # ERROR MESSAGE
                return render_to_response( 'rec_pierakst.html', args )

            if new == 0:
               # Jauns klients
                if getattr(Grafiks.objects.get( id=n_id ), 'vietas') < 1 and super != True: # IF VIETAS=0 --> ERROR
                    error = True
                    args['error_msg'] = u' Atvainojiet visas nodarbības vietas ir aizņemtas'
                else: # VIETAS > 0 --> Pieraksts
                    new_client = Klienti(vards=new_name, e_pasts=new_email, tel=new_tel, pieteikuma_reizes=1)
                    new_client.save()

                    nodarbiba = Grafiks.objects.get( id=n_id ) # VIETAS -1
                    if nodarbiba.vietas > 0:
                        nodarbiba.vietas -= 1
                    nodarbiba.save()

                    pieraksts = Pieraksti(klients=new_client, nodarbiba=nodarbiba) # PIETEIKUMS --> ACCEPT
                    pieraksts.save()
             # Pieraksts sekmigs
                    day_stat.day_stat()
                    args['vards'] = form.cleaned_data['vards']
                    args['epasts'] = form.cleaned_data['e_pasts']
                    args['telefons'] = form.cleaned_data['tel']
                    return render_to_response ('rec_pier_success.html', args )

            if error == True:
                args['error'] = True
                args['form'] = form     # ERROR MESSAGE
                return render_to_response( 'rec_pierakst.html', args )

        args['error']= True
        args['msg']= u'forma nav validēta'
        return render_to_response( 'rec_pierakst.html', args )
    return render_to_response( 'rec_pierakst.html', args )

# ========================================================================================================
