# -*- coding: utf-8 -*-
from log.models import Log

from django.contrib.auth.models import User

#from datetime import datetime

def LogEvent(user_id, event_code, event_data):
    event_code_list = [
        'Atcelts Pieraksts', 	# 0
        'Izveidots Pieraksts', 	# 1

        'Dzēsts Grafiks', 	# 2
        'Pievienots Grafiks', 	# 3

        'Dzēsts Plānotājs', 	# 4
        'Pievienots Plānotājs', # 5

        'Automātiski Atcelts Pieraksts', # 6

        'Labota Klienta Kartiņa', # 7

        'Trenera maiņa' #8
        ]
   # define string for event data
    event_data_str = ""
   # retrieve fields from event_data object
    event_fields = event_data._meta.get_fields()

    for e_field in event_fields:
        try:
            f_name = e_field.name
            data = getattr( event_data, f_name )
            event_data_str += str(data)+ ' | '
        except:
            pass

   # get User forom id
    user = User.objects.get( id = int(user_id) )

   # create Log entry
    new_entry = Log( log_user= user, log_event = event_code_list[int(event_code)], log_event_data = event_data_str)
    new_entry.save()
    return

