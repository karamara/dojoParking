# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 07:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking_spot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warnings',
            name='reported_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
