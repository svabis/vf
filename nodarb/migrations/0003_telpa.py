# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0002_auto_20170311_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telpa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telpa', models.CharField(max_length=5, choices=[(b'L', b'liel\xc4\x81 z\xc4\x81le'), (b'M', b'maz\xc4\x81 z\xc4\x81le'), (b'G', b'gym z\xc4\x81le'), (b'V', b'velo z\xc4\x81le'), (b'C', b'c\xc4\xab\xc5\x86u z\xc4\x81le')])),
            ],
            options={
                'db_table': 'telpa',
                'verbose_name': 'Telpa',
            },
        ),
    ]
