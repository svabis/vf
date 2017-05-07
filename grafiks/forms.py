# -*- coding: utf-8 -*-
from django.forms import ModelForm
from grafiks.models import Planotajs
from django import forms

# create forms here

class PlanotajsForm(ModelForm):

    chk = forms.BooleanField( required=False, widget = forms.CheckboxInput( attrs={'onclick': "showMe('diena')"} ))

    date = forms.RegexField( regex=r'^\d\d\/\d\d\/\d\d\d\d$', max_length = 10, required=True,
         error_message = (u'Ievadiet korektu datumu.'),
         widget = forms.TextInput( attrs={'class': 'form-control', 'size': 15, 'title': 'Datums'}))

    class Meta:
        model = Planotajs
        fields = ('diena', 'laiks', 'ilgums', 'nodarbiba', 'treneris', 'telpa', 'vietas')

