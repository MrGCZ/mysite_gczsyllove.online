# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-21 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truecalendar', '0017_auto_20180221_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='ispast',
            field=models.NullBooleanField(),
        ),
    ]
