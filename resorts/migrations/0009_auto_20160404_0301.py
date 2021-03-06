# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-04 03:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resorts', '0008_auto_20160403_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkiSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('weburl', models.URLField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WebCam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weburl', models.URLField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='resort',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='webcam',
            name='resort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resorts.Resort'),
        ),
        migrations.AddField(
            model_name='skischool',
            name='resort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resorts.Resort'),
        ),
    ]
