# -*- coding: utf-8 -*-
from log.models import Log

#from datetime import datetime

def LogEvent(user, event_code, event_data):
    event_code_list = [
        'Atcelts Pieraksts', # 0
        'Izveidots Pieraksts', # 1

        'Dzēsts Grafiks', # 2
        'Pievienots Grafiks', # 3

        'Dzēsts Plānotājs', # 4
        'Pievienots Plānotājs', # 5

        'Automātiski Atcelts Pieraksts', #6
        ]
   # define string for event data
    event_data_str = ""
   # retrieve fields from event_data object
    event_fields = event_data._meta.get_fields()

    for e_field in event_fields:
        f_name = e_field.name
        data = getattr( event_data, f_name )
        event_data_str += str(data)+ ' | '

    new_entry = Log(user, event_code_list[event_code], event_data_str)
    new_entry.save()
    return

