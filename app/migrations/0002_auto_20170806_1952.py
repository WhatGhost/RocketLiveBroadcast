# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 19:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveroom',
            name='room_creater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vertifyregister',
            name='vertifytime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]