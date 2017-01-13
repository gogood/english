# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_auto_20161215_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frontpageslider',
            name='picture',
        ),
        migrations.AddField(
            model_name='frontpageslider',
            name='action',
            field=models.CharField(default=b'', max_length=10, verbose_name='\u64cd\u4f5c'),
        ),
        migrations.AddField(
            model_name='frontpageslider',
            name='images',
            field=models.ImageField(default=b'', upload_to=b'static/images', verbose_name='\u56fe\u7247'),
        ),
    ]
