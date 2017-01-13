# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComboType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('combo_name', models.CharField(max_length=100, verbose_name='\u7c7b\u578b\u540d')),
                ('user', models.CharField(max_length=300, verbose_name='\u9002\u7528\u7684\u5b66\u751f')),
                ('advantage', models.CharField(max_length=1000, verbose_name='\u4f18\u52bf')),
                ('note', models.CharField(max_length=1000, verbose_name='\u6ce8\u610f')),
            ],
            options={
                'ordering': ['combo_name'],
                'verbose_name': '\u5957\u9910\u7c7b\u578b\u8868',
                'db_table': 't_combotype',
                'managed': True,
                'verbose_name_plural': '\u5957\u9910\u7c7b\u578b\u8868',
            },
        ),
        migrations.CreateModel(
            name='CountCombo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count_name', models.CharField(max_length=50, verbose_name='\u6b21\u5361\u6570\u540d\u5b57')),
                ('count_number', models.IntegerField(verbose_name='\u6b21\u5361\u6570\u91cf')),
                ('public_number', models.IntegerField(verbose_name='\u4f18\u9009\u516c\u5f00\u8bfe\u7684\u6570\u91cf')),
                ('unit', models.CharField(default=b'\xe8\xaf\xbe\xe6\x97\xb6', max_length=10, verbose_name='\u8bfe\u7684\u5355\u4f4d\uff0c\u9ed8\u8ba4\u4e3a\u8bfe\u65f6')),
                ('valid_date', models.IntegerField(verbose_name='\u6709\u6548\u671f')),
                ('money', models.IntegerField(verbose_name='\u91d1\u989d')),
                ('italk_used', models.IntegerField(verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u6570')),
                ('italk_used_unit', models.CharField(default=b'\xe6\x9c\x88', max_length=10, verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u7684\u5355\u4f4d')),
                ('present_course', models.IntegerField(verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570')),
                ('present_course_unit', models.CharField(default=b'\xe8\x8a\x82', max_length=10, verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570\u7684\u5355\u4f4d')),
                ('combo_type', models.ForeignKey(related_name='count_combo_type', verbose_name='\u6240\u5c5e\u7684\u7c7b\u578b', to='index.ComboType')),
            ],
            options={
                'ordering': ['count_name'],
                'verbose_name': '\u6b21\u5361\u5957\u9910',
                'db_table': 't_countcombo',
                'managed': True,
                'verbose_name_plural': '\u6b21\u5361\u5957\u9910',
            },
        ),
        migrations.CreateModel(
            name='FrontPageSlider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('description', models.CharField(max_length=300, verbose_name='\u63cf\u8ff0')),
                ('picture', models.FileField(upload_to=b'static/images', verbose_name='\u56fe\u7247')),
                ('url', models.URLField(verbose_name='\u94fe\u63a5')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': '\u9996\u9875\u5e7b\u706f\u7247',
                'db_table': 't_frontpagelider',
                'managed': True,
                'verbose_name_plural': '\u9996\u9875\u5e7b\u706f\u7247',
            },
        ),
        migrations.CreateModel(
            name='MonthCombo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month_name', models.CharField(max_length=100, verbose_name='\u5305\u6708\u5957\u9910\u7684\u540d\u5b57')),
                ('month_number', models.IntegerField(verbose_name='\u5305\u6708\u6570\u91cf')),
                ('valid_date', models.IntegerField(verbose_name='\u6709\u6548\u671f')),
                ('money', models.IntegerField(verbose_name='\u91d1\u989d')),
                ('italk_used', models.IntegerField(verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u6570')),
                ('italk_used_unit', models.CharField(default=b'\xe6\x9c\x88', max_length=10, verbose_name='italk\u514d\u8d39\u4f7f\u7528\u6743\u7684\u5355\u4f4d')),
                ('present_course', models.IntegerField(verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570')),
                ('present_course_unit', models.CharField(default=b'\xe8\x8a\x82', max_length=10, verbose_name='\u8d60\u9001\u8bfe\u7a0b\u6570\u7684\u5355\u4f4d')),
                ('combo_type', models.ForeignKey(related_name='month_combo_type', verbose_name='\u6240\u5c5e\u7684\u7c7b\u578b', to='index.ComboType')),
            ],
            options={
                'ordering': ['month_name'],
                'verbose_name': '\u5305\u6708\u5957\u9910',
                'db_table': 't_monthcombo',
                'managed': True,
                'verbose_name_plural': '\u5305\u6708\u5957\u9910',
            },
        ),
    ]
