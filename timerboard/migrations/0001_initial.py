# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-15 12:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sde', '0019_auto_20171231_0418'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(db_index=True)),
                ('stage', models.CharField(choices=[('AR', 'Armor'), ('ST', 'Structure')], db_index=True, max_length=2)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timers', to=settings.AUTH_USER_MODEL)),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timers', to='sde.Type')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timers', to='sde.System')),
            ],
        ),
    ]