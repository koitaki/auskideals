# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-03 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('email_collector', '0007_resort_thumbnail_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('included', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='cc_fips',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='cc_iso',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='sub_location',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resort',
            name='base_height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='resort',
            name='halfpipes',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='resort',
            name='highest_lifted_point',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='resort',
            name='lifts_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='resort',
            name='lowest_lifted_point',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='resort',
            name='season_close',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='resort',
            name='season_open',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='resort',
            name='summit_height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='resort',
            name='terrain_parks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='region',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resort',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resort',
            name='latitude',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='resort',
            name='longitude',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='resort',
            name='main_picture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='resort',
            name='thumbnail_picture',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='email_collector.Continent'),
            preserve_default=False,
        ),
    ]