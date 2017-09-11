# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-01 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restApp', '0003_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instanceID', models.CharField(max_length=10)),
                ('game', models.CharField(choices=[(b'', b'----'), (b't', b'Tourney'), (b'f', b'fake News')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('score', models.IntegerField(default=0)),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApp.Instance')),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='user',
        ),
        migrations.RemoveField(
            model_name='snippet',
            name='owner',
        ),
        migrations.DeleteModel(
            name='data',
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]