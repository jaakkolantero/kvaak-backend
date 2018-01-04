# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-04 19:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180104_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='species',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Species', to_field='name'),
        ),
        migrations.AlterField(
            model_name='species',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
