# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-06-03 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200603_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csv_file',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.user_info'),
        ),
    ]