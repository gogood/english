# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20161214_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='auto_substitute',
            field=models.CharField(max_length=10, verbose_name='\u7cfb\u7edf\u81ea\u52a8\u4ee3\u7406'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='short_message',
            field=models.CharField(max_length=10, verbose_name='\u77ed\u4fe1\u63d0\u9192'),
        ),
    ]
