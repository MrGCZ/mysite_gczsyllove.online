# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-19 05:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0029_auto_20180219_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 19, 5, 57, 11, 217257, tzinfo=utc)),
        ),
    ]