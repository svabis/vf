# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodarb', '0003_telpa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grafiks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sakums', models.DateTimeField()),
                ('vieta', models.IntegerField()),
                ('nodarbiba', models.ForeignKey(to='nodarb.Nodarb_tips')),
                ('telpa', models.ForeignKey(to='nodarb.Telpa')),
                ('treneris', models.ForeignKey(to='nodarb.Treneris')),
            ],
            options={
                'db_table': 'grafiks',
            },
        ),
    ]
