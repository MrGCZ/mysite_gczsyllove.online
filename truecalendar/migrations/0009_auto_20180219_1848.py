# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-19 10:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('truecalendar', '0008_auto_20180219_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='endate',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 19, 10, 48, 15, 392070, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='calendarevent',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 19, 10, 48, 15, 392048, tzinfo=utc)),
        ),
    ]
