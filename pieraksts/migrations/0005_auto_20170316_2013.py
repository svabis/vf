# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0003_auto_20170315_1405'),
        ('grafiks', '0006_remove_planotajs_sakums'),
        ('pieraksts', '0004_auto_20170316_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atteikumi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ateikuma_laiks', models.DateTimeField(default=django.utils.timezone.now)),
                ('klients', models.ForeignKey(to='klienti.Klienti')),
                ('nodarbiba', models.ForeignKey(to='grafiks.Grafiks')),
            ],
            options={
                'db_table': 'atteikumi',
                'verbose_name': 'Atteikumi',
            },
        ),
        migrations.AlterModelOptions(
            name='pieraksti',
            options={'verbose_name': 'Pieraksti'},
        ),
    ]
