# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PROJECT',
            fields=[
                ('project_id', models.IntegerField(primary_key=True, serialize=False, auto_created=True)),
                ('project_number', models.CharField(max_length=40)),
                ('project_name', models.CharField(max_length=100)),
                ('project_status', models.IntegerField(choices=[('01', '排产阶段'), ('02', '设计阶段'), ('03', '组屏阶段')])),
            ],
        ),
    ]
