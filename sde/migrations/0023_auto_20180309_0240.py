# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-09 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sde', '0022_auto_20180309_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeattribute',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types', to='sde.AttributeType'),
        ),
        migrations.AlterField(
            model_name='typeattribute',
            name='type',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='sde.Type'),
        ),
    ]
