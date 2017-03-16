# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django import forms

from klienti.models import *


class KlientsForm(ModelForm):
    class Meta:
        model = Klienti
        fields = ['vards', 'e_pasts', 'tel']
        labels = {
            'vards': ('Vārds Uzvārds'),
            'tel': ('Tālrunis'),
        }

        error_messages = {
            'vards': {
                'max_length': _("This writer's name is too long."),
                'required': _("Obligāti jāaizpilda"),
            },
            'tel': {
                'required': _("Oblig ^ ti j ^ aizpilda"),
            },
        }

        widgets = { 'vards': forms.TextInput( attrs={'class': 'form-control', 'size': 30, 'title': 'Vārds Uzvārds', 'required': True}), 
            'e_pasts': forms.EmailInput( attrs={'class': 'form-control', 'title': 'e-pasts', 'required': True}),
            'tel': forms.TextInput( attrs={'class': 'form-control', 'title': 'tālrunis', 'required': True}),
            }
