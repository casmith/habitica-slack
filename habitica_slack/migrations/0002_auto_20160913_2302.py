# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-13 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habitica_slack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastposttimestamp',
            name='time_stamp',
            field=models.BigIntegerField(),
        ),
    ]