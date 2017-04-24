# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0011_auto_20170416_1218'),
        ('klienti', '0011_auto_20170416_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistAtteikumi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ateikuma_laiks', models.DateTimeField(default=django.utils.timezone.now)),
                ('pieraksta_laiks', models.DateTimeField(default=django.utils.timezone.now)),
                ('klients', models.ForeignKey(to='klienti.Klienti')),
                ('nodarbiba', models.ForeignKey(to='grafiks.Grafiks')),
            ],
            options={
                'db_table': 'hist_atteikumi',
            },
        ),
        migrations.CreateModel(
            name='HistPieraksti',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pieraksta_laiks', models.DateTimeField(default=django.utils.timezone.now)),
                ('klients', models.ForeignKey(to='klienti.Klienti')),
                ('nodarbiba', models.ForeignKey(to='grafiks.Grafiks')),
            ],
            options={
                'db_table': 'hist_pieraksti',
            },
        ),
    ]
