# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-19 05:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('truecalendar', '0003_auto_20180219_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 19, 5, 52, 13, 882751, tzinfo=utc)),
        ),
    ]
