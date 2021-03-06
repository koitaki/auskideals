# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-03 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resorts', '0002_auto_20160403_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resort',
            name='base_height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='halfpipes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='highest_lifted_point',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='lifts_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='lowest_lifted_point',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='season_close',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='season_open',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='summit_height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='resort',
            name='terrain_parks',
            field=models.IntegerField(),
        ),
    ]
