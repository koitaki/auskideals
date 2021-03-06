# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-03 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resorts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resorts.Region')),
            ],
        ),
        migrations.RenameField(
            model_name='location',
            old_name='region',
            new_name='area',
        ),
        migrations.RemoveField(
            model_name='location',
            name='sub_location',
        ),
    ]
