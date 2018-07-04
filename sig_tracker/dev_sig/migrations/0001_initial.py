# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-29 17:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=2000)),
                ('summary', models.TextField(blank=True)),
                ('contact', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]