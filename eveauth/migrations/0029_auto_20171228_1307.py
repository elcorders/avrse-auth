# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-28 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0028_auto_20171228_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='fatigue_expire_date',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='last_jump_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
