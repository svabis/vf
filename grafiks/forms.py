# -*- coding: utf-8 -*-
from django.forms import ModelForm
from grafiks.models import Planotajs
from django import forms

# create forms here

class PlanotajsForm(ModelForm):
    class Meta:
        model = Planotajs
        fields = ('diena', 'laiks', 'ilgums', 'nodarbiba', 'treneris', 'telpa', 'vietas')

#        jobs_date_added = forms.DateTimeField(widget=forms.widgets.DateTimeInput(input_formats=["%d %b %Y %H:%M:%S %Z"]))

#        widgets = {'jobs_date_added': forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={'class': 'form-control'}),
#			'jobs_descr': forms.Textarea(attrs={'class': 'form-control', 'rows' : '3'}),
#			'jobs_zone': forms.Select(attrs={'class': 'form-control'}),
#			'jobs_type': forms.Select(attrs={'class': 'form-control'}),
#			}
