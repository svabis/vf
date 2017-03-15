# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import grafiks.models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0006_auto_20170311_1644'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grafiks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sakums', models.DateTimeField()),
                ('ilgums', models.IntegerField()),
                ('vietas', models.IntegerField()),
                ('nodarbiba', models.ForeignKey(to='nodarb.Nodarb_tips')),
                ('telpa', models.ForeignKey(to='nodarb.Telpa')),
                ('treneris', models.ForeignKey(to='nodarb.Treneris')),
            ],
            options={
                'db_table': 'grafiks',
            },
        ),
        migrations.CreateModel(
            name='Planotajs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sakums', models.DateTimeField()),
#                ('diena', models.IntegerField(default=0)),
#                ('laiks', models.TimeField(default=grafiks.models.default_start_time)),
                ('ilgums', models.IntegerField(default=55)),
                ('vietas', models.IntegerField()),
                ('nodarbiba', models.ForeignKey(to='nodarb.Nodarb_tips')),
                ('telpa', models.ForeignKey(to='nodarb.Telpa')),
                ('treneris', models.ForeignKey(to='nodarb.Treneris')),
            ],
            options={
                'db_table': 'planotajs',
            },
        ),
    ]
