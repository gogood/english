# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0031_auto_20170112_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=100000, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0'),
        ),
    ]
