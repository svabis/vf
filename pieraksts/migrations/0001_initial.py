# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0003_auto_20170315_1405'),
        ('grafiks', '0006_remove_planotajs_sakums'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pieraksti',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pieraksta_laiks', models.DateTimeField(default=django.utils.timezone.now)),
                ('klients', models.ForeignKey(to='klienti.Klienti')),
                ('nodarbiba', models.ForeignKey(to='grafiks.Grafiks')),
            ],
            options={
                'db_table': 'pieraksti',
            },
        ),
    ]
