# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nodarb_tips',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nos', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('apraksts', models.TextField(default=b'')),
            ],
            options={
                'db_table': 'nodarb_tips',
            },
        ),
        migrations.CreateModel(
            name='Tren_nodarb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nodarb', models.ForeignKey(to='nodarb.Nodarb_tips')),
            ],
            options={
                'db_table': 'tren_nodarb',
            },
        ),
        migrations.CreateModel(
            name='Treneris',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vards', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('apraksts', models.TextField(default=b'')),
            ],
            options={
                'db_table': 'treneris',
            },
        ),
        migrations.AddField(
            model_name='tren_nodarb',
            name='treneris',
            field=models.ForeignKey(to='nodarb.Treneris'),
        ),
    ]
