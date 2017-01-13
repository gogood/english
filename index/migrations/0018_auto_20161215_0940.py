# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_auto_20161215_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontpageslider',
            name='picture',
            field=models.ImageField(upload_to=b'static/images', verbose_name='\u56fe\u7247'),
        ),
        migrations.AlterField(
            model_name='student',
            name='card_number',
            field=models.PositiveIntegerField(verbose_name='\u5269\u4f59\u6b21\u5361\u6570'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lv',
            field=models.PositiveIntegerField(verbose_name='\u82f1\u8bed\u6c34\u5e73'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.PositiveIntegerField(max_length=11, verbose_name='\u624b\u673a'),
        ),
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(upload_to=b'static/images', verbose_name='\u5934\u50cf'),
        ),
        migrations.AlterField(
            model_name='student',
            name='study_number',
            field=models.PositiveIntegerField(verbose_name='\u5b66\u8c46\u6570\u91cf'),
        ),
    ]
