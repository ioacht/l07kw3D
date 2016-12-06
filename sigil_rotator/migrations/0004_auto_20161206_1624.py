# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-06 16:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sigil_rotator', '0003_auto_20161206_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sigil',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]