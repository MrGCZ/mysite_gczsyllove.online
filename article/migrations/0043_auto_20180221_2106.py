# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-21 13:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0042_auto_20180221_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 21, 13, 6, 0, 716949, tzinfo=utc)),
        ),
    ]
