# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0010_nodarb_tips_izcelt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodarb_tips',
            name='redz',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='telpa',
            name='telpa',
            field=models.CharField(max_length=5, choices=[(b'L', b'Liel\xc4\x81 z\xc4\x81le'), (b'M', b'Maz\xc4\x81 z\xc4\x81le'), (b'G', b'Gym z\xc4\x81le'), (b'V', b'Velo z\xc4\x81le'), (b'C', b'C\xc4\xab\xc5\x86u z\xc4\x81le')]),
        ),
    ]
