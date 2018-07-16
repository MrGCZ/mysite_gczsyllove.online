# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-19 10:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('truecalendar', '0010_auto_20180219_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarevent',
            name='date',
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='begindate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 19, 10, 58, 41, 715591, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='importance',
            field=models.CharField(choices=[(1, 'Important'), (2, 'Fairly Important'), (3, 'Very Important'), (4, 'Specially Important'), (5, 'Extremly Important')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='calendarevent',
            name='endate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 19, 10, 58, 41, 715617, tzinfo=utc)),
        ),
    ]
