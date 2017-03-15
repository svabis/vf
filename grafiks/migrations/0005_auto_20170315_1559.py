# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0004_auto_20170315_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planotajs',
            name='diena',
            field=models.CharField(default=0, max_length=1, choices=[(b'0', b'P'), (b'1', b'O'), (b'2', b'T'), (b'3', b'C'), (b'4', b'Pk'), (b'5', b'S'), (b'6', b'Sv')]),
        ),
    ]
