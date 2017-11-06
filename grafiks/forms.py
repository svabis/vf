# -*- coding: utf-8 -*-
from django.forms import ModelForm

from grafiks.models import Planotajs
from nodarb.models import *

from django import forms


# !!!!! Planotajs Form !!!!!
class PlanotajsForm(ModelForm):

    nodarbiba = forms.ModelChoiceField( queryset = Nodarb_tips.objects.all().order_by('nos'),
         widget = forms.Select( attrs={'class': 'form-control'}))

    treneris = forms.ModelChoiceField( queryset = Treneris.objects.all().order_by('vards'),
         widget = forms.Select( attrs={'class': 'form-control'}))

    chk = forms.BooleanField( required=False, widget = forms.CheckboxInput( attrs={'onclick': "showMe('diena')"} ))

    date = forms.RegexField( regex=r'^\d\d\/\d\d\/\d\d\d\d$', max_length = 10, required=True,
         error_message = (u'Ievadiet korektu datumu.'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'Datums'}))

    end_date = forms.RegexField( regex=r'^\d\d\/\d\d\/\d\d\d\d$', max_length = 10, required=False,
         error_message = (u'Ievadiet korektu datumu.'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'Datums'}))

    laiks = forms.RegexField( regex=r'^\d\d\:\d\d$', required=True, error_message = (u'Ievadiet korektu laiku.'), initial="08:00",
         widget = forms.TextInput( attrs={'class': 'form-control', 'title': 'Sākums'}))

    class Meta:
        model = Planotajs
        fields = ('diena', 'ilgums', 'telpa', 'vietas' ) # , 'laiks' )

        widgets = {
            'diena': forms.Select(attrs={'class': 'form-control'}),
            'ilgums': forms.NumberInput(attrs={'class': 'form-control'}),
            'telpa': forms.Select(attrs={'class': 'form-control'}),
            'vietas': forms.NumberInput(attrs={'class': 'form-control'}),
            }


# !!!!! TrenRelForm !!!!!
#class TrenRelForm(ModelForm):
class TrenRelForm(forms.Form):

#    nodarb = forms.ModelChoiceField( queryset = Nodarb_tips.objects.all().order_by('nos') )

    treneris = forms.ModelChoiceField( queryset = Treneris.objects.all().order_by('vards') )

#    class Meta:
#        model = Tren_nodarb
#        fields = ( 'treneris', 'nodarb' )
#        exclude = ( 'treneris', 'nodarb' )
