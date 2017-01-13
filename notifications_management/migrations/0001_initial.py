# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='\u6807\u9898')),
                ('content', models.TextField(max_length=100000, verbose_name='\u6b63\u6587')),
                ('create_at', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('category', models.CharField(max_length=30, verbose_name='\u5206\u7c7b', choices=[('0', '\u6559\u52a1\u5904\u901a\u77e5'), ('1', '\u4e8c\u7ea7\u5b66\u9662\u6559\u5b66\u79d8\u4e66\u901a\u77e5')])),
            ],
            options={
                'verbose_name': '\u901a\u77e5\u516c\u544a',
                'db_table': 't_notifications',
                'managed': True,
                'verbose_name_plural': '\u901a\u77e5\u516c\u544a',
            },
        ),
    ]
