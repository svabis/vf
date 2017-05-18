# -*- coding: utf-8 -*-
from django.forms import ModelForm

from grafiks.models import Planotajs
from nodarb.models import *

from django import forms


# !!!!! Planotajs Form !!!!!
class PlanotajsForm(ModelForm):

    nodarbiba = forms.ModelChoiceField( queryset = Nodarb_tips.objects.all() )
#    treneris = forms.ModelChoiceField( queryset = Treneris.objects.filter( t = nodarbiba ) )

    chk = forms.BooleanField( required=False, widget = forms.CheckboxInput( attrs={'onclick': "showMe('diena')"} ))

    date = forms.RegexField( regex=r'^\d\d\/\d\d\/\d\d\d\d$', max_length = 10, required=True,
         error_message = (u'Ievadiet korektu datumu.'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'Datums'}))

    class Meta:
        model = Planotajs
        fields = ('diena', 'laiks', 'ilgums', 'telpa', 'vietas', 'treneris' ) # 'nodarbiba'


# !!!!! TrenRelForm !!!!!
class TrenRelForm(ModelForm):
    class Meta:
        model = Tren_nodarb
        fields = ( 'treneris', 'nodarb' )
