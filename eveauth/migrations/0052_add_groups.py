# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-11 05:38
from __future__ import unicode_literals

from django.db import migrations


def add_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")

    logistics, logistics_created = Group.objects.get_or_create(name="Logistics")
    audit, audit_created = Group.objects.get_or_create(name="Audit")

    if logistics_created:
        logistics.details.is_open = False
        logistics.details.can_apply = True
        logistics.details.forum = True
        logistics.details.discord = True
        logistics.details.save()

    if audit_created:
        audit.details.is_open = False
        audit.details.can_apply = True
        audit.details.forum = True
        audit.details.discord = True
        audit.details.save()


class Migration(migrations.Migration):

    dependencies = [
        ('eveauth', '0051_structure_fuel_expires'),
    ]

    operations = [
        migrations.RunPython(add_groups),
    ]
