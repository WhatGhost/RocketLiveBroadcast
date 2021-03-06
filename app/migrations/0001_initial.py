# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 15:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('account', models.CharField(max_length=250, unique=True)),
                ('nickname', models.CharField(max_length=200)),
                ('is_student', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AllSilent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('is_allsilent', models.BooleanField()),
                ('silent_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('user', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('room_id', models.IntegerField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=100)),
                ('room_introduction', models.TextField(null=True)),
                ('room_img', models.ImageField(upload_to='img/covers')),
                ('room_creater', models.CharField(max_length=100)),
                ('history_source', models.FileField(null=True, upload_to='video')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('time_length', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LiveRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=100)),
                ('room_introduction', models.TextField(null=True)),
                ('room_img', models.ImageField(null=True, upload_to='img/covers')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('active_mode', models.CharField(default='READY', max_length=10)),
                ('room_creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OneSilent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('user', models.CharField(max_length=100)),
                ('is_silent', models.BooleanField()),
                ('silent_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_slide', models.FileField(upload_to='slide/orginal')),
                ('converted_pdf', models.FileField(null=True, upload_to='slide/pdf')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('live_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.LiveRoom')),
            ],
        ),
        migrations.CreateModel(
            name='VertifyForgetpasswd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100)),
                ('vertifycode', models.CharField(max_length=100)),
                ('vertifytime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VertifyRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100)),
                ('vertifycode', models.CharField(max_length=100)),
                ('vertifytime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='VisitHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('user', models.CharField(max_length=100)),
                ('visit_time', models.DateTimeField()),
                ('leave_time', models.DateTimeField()),
                ('is_refused', models.BooleanField()),
            ],
        ),
    ]
