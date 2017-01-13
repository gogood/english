# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0030_auto_20170112_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0'),
        ),
    ]
