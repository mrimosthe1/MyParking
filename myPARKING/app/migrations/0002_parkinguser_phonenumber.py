# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkinguser',
            name='phonenumber',
            field=models.IntegerField(default=8675309, max_length=12),
        ),
    ]
