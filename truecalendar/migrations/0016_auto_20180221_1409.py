# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-02-21 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truecalendar', '0015_auto_20180219_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendarevent',
            options={'ordering': ('-importance', '-created')},
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='done',
            field=models.NullBooleanField(),
        ),
    ]