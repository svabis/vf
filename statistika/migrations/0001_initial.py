# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayPierStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x', models.IntegerField(default=0)),
                ('y', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dienas_stat_dati',
            },
        ),
    ]
