# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-21 06:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0040_auto_20180219_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 21, 6, 9, 13, 905220, tzinfo=utc)),
        ),
    ]
