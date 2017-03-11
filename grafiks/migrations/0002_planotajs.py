# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0004_auto_20170311_1447'),
        ('grafiks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planotajs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sakums', models.DateTimeField()),
                ('vieta', models.IntegerField()),
                ('nodarbiba', models.ForeignKey(to='nodarb.Nodarb_tips')),
                ('telpa', models.ForeignKey(to='nodarb.Telpa')),
                ('treneris', models.ForeignKey(to='nodarb.Treneris')),
            ],
            options={
                'db_table': 'planotajs',
            },
        ),
    ]
