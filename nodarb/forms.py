# -*- coding: utf-8 -*-
from django.forms import ModelForm

from nodarb.models import *

from django import forms
from django.utils.translation import ugettext_lazy

# Treneris Form
class TrenerisForm(ModelForm):
    class Meta:
        model = Treneris
        fields = ('vards', 'apraksts', 'avatar',) # slug

        widgets = {
            'vards': forms.TextInput( attrs={'class': 'form-control', 'size': 30 }),
            'apraksts': forms.Textarea(attrs={'class': 'form-control', 'rows' : '3'}),
            'avatar': forms.Select(attrs={'class': 'form-control'}),
            }


# Nodarb_tips Form
class Nodarb_tipsForm(ModelForm):
    class Meta:
        model = Nodarb_tips
        fields = ('nos', 'izcelt', 'apraksts') # slug, redz

        nos = forms.CharField(required = True, error_messages = {'required': ugettext_lazy(u'Obligāts jāaizpilda')})

        widgets = {
            'nos': forms.TextInput( attrs={'class': 'form-control', 'size': 30 }),
            'apraksts': forms.Textarea(attrs={'class': 'form-control', 'rows' : '10'}),
            'izcelt': forms.CheckboxInput(attrs={'class': 'form-control'})
            }
