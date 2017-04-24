#!/usr/bin/python2
# -*- coding: utf-8 -*-
from statistika.models import DayPierStat

import datetime

def day_stat():
    time = datetime.datetime.now()

    time_h = int(time.hour) * 60
    time_m = int(time.minute)
    time_x = (time_h + time_m) / 10

    count = 0 # counter to chech object existence

# define django object
    st = DayPierStat.objects.all()

    for s in st:
        if s.x == time_x:
            s.y += 1
            s.save()
            count += 1

    if count == 0:
        new_st = DayPierStat( x=time_x, y=1 )
        new_st.save()
