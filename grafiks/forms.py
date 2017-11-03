# -*- coding: utf-8 -*-
from django.forms import ModelForm

from grafiks.models import Planotajs
from nodarb.models import *

from django import forms


# !!!!! Planotajs Form !!!!!
class PlanotajsForm(ModelForm):

    nodarbiba = forms.ModelChoiceField( queryset = Nodarb_tips.objects.all().order_by('nos') )

    treneris = forms.ModelChoiceField( queryset = Treneris.objects.all().order_by('vards') )

    chk = forms.BooleanField( required=False, widget = forms.CheckboxInput( attrs={'onclick': "showMe('diena')"} ))

    date = forms.RegexField( regex=r'^\d\d\/\d\d\/\d\d\d\d$', max_length = 10, required=True,
         error_message = (u'Ievadiet korektu datumu.'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'Datums'}))

    end_date = forms.RegexField( regex=r'^\d\d\/\d\d\/\d\d\d\d$', max_length = 10, required=False,
         error_message = (u'Ievadiet korektu datumu.'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'Datums'}))

    class Meta:
        model = Planotajs
        fields = ('diena', 'laiks', 'ilgums', 'telpa', 'vietas' ) #, 'treneris' )


# !!!!! TrenRelForm !!!!!
class TrenRelForm(ModelForm):

    nodarb = forms.ModelChoiceField( queryset = Nodarb_tips.objects.all().order_by('nos') )

    treneris = forms.ModelChoiceField( queryset = Treneris.objects.all().order_by('vards') )

    class Meta:
        model = Tren_nodarb
        fields = ( 'treneris', 'nodarb' )
        exclude = ( 'treneris', 'nodarb' )
