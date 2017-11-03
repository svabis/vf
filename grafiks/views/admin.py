# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect	# response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth # autorisation library
from django.contrib.auth.models import User, Group

from django.core.context_processors import csrf

#from pieraksts.models import *
#from grafiks.models import Grafiks, Planotajs
#from grafiks.forms import *
#from nodarb.models import *

#from main import mail

#import os
import datetime
today = datetime.date.today()


def kalend(request):
    username = auth.get_user(request)
    if username.is_superuser or username.groups.filter(name='administrator').exists(): # SUPERUSER vai "administrator" Grupa
        args = {}
        args['admin'] = True
        args['today'] = today
        return render_to_response ( 'kalend.html', args )
    return redirect('/reception/login/')
