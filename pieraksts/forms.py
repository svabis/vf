# -*- coding: utf-8 -*-
from django import forms
from klienti.models import *

from django.utils.translation import ugettext_lazy

# !!!!! KlientsForm --> Pieraksts
class KlientsForm(forms.Form):
    vards = forms.RegexField( regex=r'^\D{3,15}\s\D+$',
        error_message = (u'Obligāti jāievada Vārds un Uzvārds'),
        widget = forms.TextInput( attrs={'class': 'form-control', 'size': 30, 'title': 'Vārds Uzvārds'}))

    e_pasts = forms.EmailField( required=True,
         widget = forms.EmailInput( attrs={'class': 'form-control', 'title': 'e-pasts'}))

    tel = forms.RegexField( regex=r'^[+]\d+|\d+', max_length = 15, required=True,
         error_message = (u'Ievadiet korektu Tālruņa numuru'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'tālrunis'}))

    chk = forms.BooleanField( required = True, error_messages = {'required': ugettext_lazy(u'Jāpiekrīt Noteikumiem')},
         widget = forms.CheckboxInput( ))


# !!!!! KlientsReceptionForm --> Reception
class KlientsReceptionForm(forms.Form):
    vards = forms.RegexField( regex=r'^\D{3,15}\s\D+$',
        error_message = (u'Obligāti jāievada Vārds un Uzvārds'),
        widget = forms.TextInput( attrs={'class': 'form-control', 'size': 30, 'title': 'Vārds Uzvārds'}))

    e_pasts = forms.EmailField( required=False,
         widget = forms.EmailInput( attrs={'class': 'form-control', 'title': 'e-pasts'}))

    tel = forms.RegexField( regex=r'^[+]\d{14}|\d{15}|$', max_length = 15, required=True,
         error_message = (u'Tālruņa nummuram ir jāsākas ar 2 vai 6, ciparu skaitam ir jābūt 8.'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'tālrunis'}))
