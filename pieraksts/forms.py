# -*- coding: utf-8 -*-
from django import forms
from klienti.models import *

# form error message override
from django.forms import Field
from django.utils.translation import ugettext_lazy

#Field.default_error_messages = { 'required': ugettext_lazy(u'šis lauks ir jāaizpilda obligāti') }

class KlientsForm(forms.Form):
    vards = forms.RegexField( regex=r'^\D{3,15}\s\D+$', label = u'Vārds Uzvārds',
        error_message = (u'Obligāti jāievada Vārds un Uzvārds'),
        widget = forms.TextInput( attrs={'class': 'form-control', 'size': 30, 'title': 'Vārds Uzvārds'}))

    e_pasts = forms.EmailField( required=True, label = u'E-pasts',
         widget = forms.EmailInput( attrs={'class': 'form-control', 'title': 'e-pasts'}))

    tel = forms.RegexField( regex=r'^[+]\d{14}|\d{15}|$', max_length = 15, label = u'Tālrunis', required=False,
         error_message = (u'Tālruņa nummuram ir jāsākas ar 2 vai 6, ciparu skaitam ir jābūt 8.'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'tālrunis'}))

    chk = forms.BooleanField( required = True, label ='', error_messages = {'required': ugettext_lazy(u'Jāpiekrīt Noteikumiem')},
         widget = forms.CheckboxInput( attrs={'class':'form-control', 'align':'left'}))
