# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-26 15:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_auto_20171112_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, max_length=100)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('profession', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('aboutme', models.CharField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
