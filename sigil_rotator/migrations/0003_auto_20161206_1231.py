# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigil_rotator', '0002_auto_20161206_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sigil',
            name='end_date',
            field=models.DateTimeField(verbose_name='end_date'),
        ),
        migrations.AlterField(
            model_name='sigil',
            name='upload_date',
            field=models.DateTimeField(verbose_name='upload_date'),
        ),
    ]
