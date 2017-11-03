# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

# Login
    url(r'^login/$', 'grafiks.views.login'),
    url(r'^logout/$', 'grafiks.views.logout'),

# ---------------------------------------- MAIN SADAĻA -----------------------------------------------
# Reception History
    url(r'^hist/$', 'grafiks.views.history'),
    url(r'^hist/(?P<date>\d+\/\d+\/\d+)/$', 'grafiks.views.hist_date', name='hist_date'),
    url(r'^hist/(?P<date>\d+\/\d+\/\d+)/(?P<g_id>\d+)/p/$', 'grafiks.views.hist_date_kli'),
    url(r'^hist/(?P<date>\d+\/\d+\/\d+)/(?P<g_id>\d+)/c/$', 'grafiks.views.hist_date_cancel'),

# Reception Pieraksts
    url(r'^pierakstities/(?P<d_id>\d+)/(?P<n_id>\d+)/$', 'grafiks.views.reception_pieraksts'),
# Reception Cancel
    url(r'^cancel/(?P<d_id>\d+)/(?P<g_id>\d+)/(?P<p_id>\d+)/$', 'grafiks.views.reception_cancel'),

# Nodarbibu Tab skati
    url(r'^nod/(?P<d_id>\d+)/(?P<g_id>\d+)/$', 'grafiks.views.nod_list', name='nod_list'),
    url(r'^atteikumi/(?P<d_id>\d+)/(?P<g_id>\d+)/$', 'grafiks.views.cancel_list'),
    url(r'^day/(?P<d_id>\d+)/$', 'grafiks.views.day_list', name='day_list'),
# Reception Print
    url(r'^print_nod/(?P<d_id>\d+)/(?P<g_id>\d+)/$', 'grafiks.views.print_nod'),

# Klientu saraksts
    url(r'^klienti/(?P<search>[-\w]+)$', 'grafiks.views.klienti', name='klienti'),
    url(r'^klienti/$', 'grafiks.views.klienti', name='klienti'),
# Klienta kartiņas edit
    url(r'^klients/$', 'grafiks.views.klients_edit'),


# -------------------------------------- SUPERUSER SADAĻA --------------------------------------------

# Nodarbibu ATCELŠANA
    url(r'^graf/(?P<w_id>\d+)/$', 'grafiks.views.week_list', name="nod_plan"),
    url(r'^graf/(?P<w_id>\d+)/cancel/(?P<g_id>\d+)/$', 'grafiks.views.graf_cancel'),
    url(r'^graf/$', 'grafiks.views.graf_list'),

# Grafika izmaiņas - Atcelšana
    url(r'^plan/$', 'grafiks.views.plan_list', name="plan_list"),


# Treneru aizvietosan
    url(r'^tren/(?P<w_id>\d+)/$', 'grafiks.views.tren_week_list', name="tren_week_list"),
    url(r'^tren/(?P<w_id>\d+)/replace/(?P<g_id>\d+)/$', 'grafiks.views.tren_aizv'),
    url(r'^tren/$', 'grafiks.views.tren_list'),

# Treneru aizvietošana sākot no datuma + Planotājā

# Treneru kartiņas edit
    url(r'^treneri/$', 'grafiks.views.treneri_edit'),


# Nodarbibas pievienoshana
    url(r'^add/$', 'grafiks.views.graf_add'),

# Nodarbību kartiņu edit
    url(r'^nodarbibas/$', 'grafiks.views.nodarbibas_edit'),


# Kalendāra skats
    url(r'^kalendar/$', 'grafiks.views.kalend'),

# Main --> Shodienas nodarbibas
    url(r'^$', 'grafiks.views.main'),
]
