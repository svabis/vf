# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [

# Nodarbību atcelšanas e-pasta linki
    url(r'^atcelt/(?P<id>[-\w]+)/$', 'pieraksts.views.cancel'), # pieraksta atcelshana
#    url(r'^atcelts/(?P<id>[-\w]+)/$', 'pieraksts.views.cancel_ok'), # pieraksta atcelshana
    url(r'^atcelts/$', 'pieraksts.views.cancel_ok'), # pieraksta atcelshana

# ==================================
# From main -->  1. main,   2.select/,   3.select/any/
    url(r'^tren/(?P<n_id>[-\w]+)/$', 'pieraksts.views.tren'), # treneris choise

# Nodarbības izvēle
    url(r'^select/(?P<n_id>[-\w]+)/any/$', 'pieraksts.views.any', name='any'), # any trainer
    url(r'^select/(?P<n_id>[-\w]+)/(?P<t_id>[-\w]+)/$', 'pieraksts.views.specific', name='specific'), # specific trainer

# Pieraksts uz nodarbību Forma
    url(r'^pieraksts/(?P<g_id>\d+)/$', 'pieraksts.views.pieraksts'), # pieraksts

# MAIN skats
    url(r'^', 'pieraksts.views.home', name='main'),

]

