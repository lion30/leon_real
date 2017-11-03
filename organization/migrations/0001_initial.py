# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ornanization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('duty', models.CharField(max_length=20)),
                ('cell_phone', models.IntegerField(max_length=11)),
                ('plane_number', models.IntegerField(max_length=11)),
            ],
        ),
    ]
