# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_parkinguser_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkinguser',
            name='phonenumber',
            field=models.IntegerField(default=8675309),
        ),
    ]