# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grafiks', '0003_planotajs_laiks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planotajs',
            name='diena',
            field=models.IntegerField(default=0, choices=[(b'0', b'P'), (b'1', b'O'), (b'2', b'T'), (b'3', b'C'), (b'4', b'Pk'), (b'5', b'S'), (b'6', b'Sv')]),
        ),
    ]
