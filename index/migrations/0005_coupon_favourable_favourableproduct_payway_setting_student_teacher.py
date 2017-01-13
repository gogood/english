# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20161214_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coupon_id', models.IntegerField(verbose_name='\u4ee3\u91d1\u5238\u7684\u7f16\u53f7')),
                ('coupon_money', models.IntegerField(verbose_name='\u4ee3\u91d1\u5238\u7684\u91d1\u989d')),
                ('valid_date', models.DateField()),
                ('state', models.IntegerField(verbose_name='\u4ee3\u91d1\u5238\u7684\u72b6\u6001\uff0c1\u8868\u793a\u672a\u4f7f\u7528\uff0c2\u8868\u793a\u5df2\u4f7f\u7528\uff0c3\u8868\u793a\u5df2\u8fc7\u671f')),
            ],
            options={
                'ordering': ['coupon_money'],
                'verbose_name': '\u4ee3\u91d1\u5238',
                'db_table': 't_coupon',
                'managed': True,
                'verbose_name_plural': '\u4ee3\u91d1\u5238',
            },
        ),
        migrations.CreateModel(
            name='Favourable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favourable_id', models.IntegerField(verbose_name='\u4f18\u60e0\u7f16\u53f7')),
                ('favourable_money', models.IntegerField(verbose_name='\u4f18\u60e0\u91d1\u989d')),
                ('favourable_description', models.CharField(max_length=300, verbose_name='\u4f18\u60e0\u63cf\u8ff0')),
            ],
            options={
                'ordering': ['favourable_money'],
                'verbose_name': '\u4f18\u60e0\u8868',
                'db_table': 't_favourable',
                'managed': True,
                'verbose_name_plural': '\u4f18\u60e0\u8868',
            },
        ),
        migrations.CreateModel(
            name='FavourableProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=100, verbose_name='\u4f18\u60e0\u4ea7\u54c1\u540d')),
                ('product_price', models.IntegerField(verbose_name='\u4f18\u60e0\u4ef7\u683c')),
            ],
            options={
                'ordering': ['product_price'],
                'verbose_name': '\u4f18\u60e0\u4ea7\u54c1\u8868',
                'db_table': 't_favourableproduct',
                'managed': True,
                'verbose_name_plural': '\u4f18\u60e0\u4ea7\u54c1\u8868',
            },
        ),
        migrations.CreateModel(
            name='PayWay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pay_way_type', models.IntegerField(default=2, verbose_name='\u6536\u8d39\u65b9\u5f0f\uff0c1\u8868\u793a12\u6708\u5206\u671f\u4ed8\u6b3e\uff0c2\u8868\u793a\u4e00\u6b21\u6027\u4ed8\u6e05')),
                ('pay_platform', models.CharField(max_length=300, verbose_name='\u6536\u8d39\u5e73\u53f0')),
            ],
            options={
                'ordering': ['pay_way_type'],
                'verbose_name': '\u4ed8\u8d39\u65b9\u5f0f\u8868',
                'db_table': 't_payway',
                'managed': True,
                'verbose_name_plural': '\u4ed8\u8d39\u65b9\u5f0f\u8868',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_message', models.IntegerField(default=1, verbose_name='\u77ed\u4fe1\u63d0\u9192\uff0c1\u8868\u793a\u63d0\u9192\uff0c2\u8868\u793a\u4e0d\u63d0\u9192')),
                ('auto_substitute', models.IntegerField(default=1, verbose_name='\u7cfb\u7edf\u81ea\u52a8\u4ee3\u7406\uff0c1\u8868\u793a\u542f\u52a8\uff0c2\u8868\u793a\u5173\u95ed')),
            ],
            options={
                'ordering': ['short_message'],
                'verbose_name': '\u4e0a\u8bfe\u8bbe\u7f6e\u8868',
                'db_table': 't_setting',
                'managed': True,
                'verbose_name_plural': '\u4e0a\u8bfe\u8bbe\u7f6e\u8868',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_id', models.IntegerField(verbose_name='\u5b66\u53f7')),
                ('lv', models.IntegerField(verbose_name='\u82f1\u8bed\u6c34\u5e73')),
                ('study_number', models.IntegerField(verbose_name='\u5b66\u8c46\u6570\u91cf')),
                ('card_number', models.IntegerField(verbose_name='\u5269\u4f59\u6b21\u5361\u6570')),
                ('english_name', models.CharField(max_length=50, verbose_name='\u82f1\u6587\u540d\u5b57')),
                ('true_name', models.CharField(max_length=50, verbose_name='\u771f\u5b9e\u59d3\u540d')),
                ('phone', models.IntegerField(verbose_name='\u7535\u8bdd\u6216\u624b\u673a')),
                ('picture', models.FileField(upload_to=b'static/images', verbose_name='\u5934\u50cf')),
                ('sex', models.CharField(max_length=10, verbose_name='\u6027\u522b')),
                ('qq', models.IntegerField(verbose_name='QQ')),
                ('birthday', models.DateField(verbose_name='\u751f\u65e5')),
                ('recepient', models.CharField(max_length=50, verbose_name='\u6536\u4ef6\u4eba\u7684\u59d3\u540d')),
                ('post_code', models.IntegerField(verbose_name='\u90ae\u7f16')),
                ('address', models.CharField(max_length=100, verbose_name='\u6536\u4ef6\u4eba\u7684\u5730\u5740')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5b66\u5458\u8868',
                'db_table': 't_student',
                'managed': True,
                'verbose_name_plural': '\u5b66\u5458\u8868',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_name', models.CharField(max_length=100, verbose_name='\u5916\u6559\u540d')),
                ('picture', models.FileField(upload_to=b'static/images', verbose_name='\u5934\u50cf')),
                ('motto', models.CharField(max_length=300, verbose_name='\u94ed\u8a00')),
                ('be_good_at_course', models.CharField(max_length=100, verbose_name='\u64c5\u957f\u7684\u8bfe\u7a0b')),
                ('student_lv', models.CharField(max_length=100, verbose_name='\u9002\u5408\u6559\u5b66\u5458\u7684\u7ea7\u522b')),
                ('teacher_experience', models.CharField(max_length=100, verbose_name='\u6559\u5b66\u7ecf\u9a8c')),
                ('hobby', models.CharField(max_length=300, verbose_name='\u5174\u8da3\u7231\u597d')),
                ('constellation', models.CharField(max_length=100, verbose_name='\u661f\u5ea7')),
                ('major', models.CharField(max_length=100, verbose_name='\u5927\u5b66\u4e13\u4e1a')),
                ('work_industry', models.CharField(max_length=100, verbose_name='\u5de5\u4f5c\u884c\u4e1a')),
                ('star_number', models.IntegerField(verbose_name='\u661f\u661f\u6570')),
                ('flowers_number', models.IntegerField(verbose_name='\u732e\u82b1\u6570')),
                ('shared_number', models.IntegerField(verbose_name='\u5206\u4eab\u7c79')),
                ('introduction', models.CharField(max_length=500, verbose_name='\u81ea\u6211\u4ecb\u7ecd')),
                ('dynamic', models.CharField(max_length=1000, verbose_name='\u5916\u6559\u52a8\u6001')),
            ],
            options={
                'ordering': ['teacher_experience'],
                'verbose_name': '\u5916\u6559',
                'db_table': 't_teacher',
                'managed': True,
                'verbose_name_plural': '\u5916\u6559',
            },
        ),
    ]
