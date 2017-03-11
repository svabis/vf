# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klienti',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pirmais_pieteikums', models.DateTimeField(default=django.utils.timezone.now)),
                ('pedejais_pieteikums', models.DateTimeField()),
                ('vards', models.CharField(default=b'', max_length=50)),
                ('e_pasts', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('pieteikuma_reizes', models.IntegerField()),
            ],
            options={
                'db_table': 'klienti',
                'verbose_name': 'Klienti',
            },
        ),
    ]
