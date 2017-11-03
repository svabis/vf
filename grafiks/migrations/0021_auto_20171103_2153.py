# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0020_planotajs_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planotajs',
            name='diena',
            field=models.CharField(default=0, max_length=15, choices=[(b'0', b'Pirmdiena'), (b'1', b'Otrdiena'), (b'2', b'Tre\xc5\xa1diena'), (b'3', b'Ceturtdiena'), (b'4', b'Piektdiena'), (b'5', b'Sestsdiena'), (b'6', b'Sv\xc4\x93tdiena')]),
        ),
    ]
