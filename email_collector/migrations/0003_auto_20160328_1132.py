# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-28 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_collector', '0002_auto_20160328_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospectiveuser',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
