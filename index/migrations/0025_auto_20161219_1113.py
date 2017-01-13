# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0024_auto_20161217_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u8bfe\u7a0b\u5206\u7c7b\u8868',
                'db_table': 't_coursecategory',
                'managed': True,
                'verbose_name_plural': '\u8bfe\u7a0b\u5206\u7c7b\u8868',
            },
        ),
        migrations.CreateModel(
            name='DetailCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u8be6\u7ec6\u5206\u7c7b',
                'db_table': 't_detailcategory',
                'managed': True,
                'verbose_name_plural': '\u8be6\u7ec6\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('main_name', models.CharField(max_length=20, verbose_name='\u4e3b\u5206\u7c7b\u540d')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u4e3b\u5206\u7c7b\u8868',
                'db_table': 't_maincategory',
                'managed': True,
                'verbose_name_plural': '\u4e3b\u5206\u7c7b\u8868',
            },
        ),
        migrations.CreateModel(
            name='SmallCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('small_name', models.CharField(max_length=20, verbose_name='\u5c0f\u5206\u7c7b\u540d')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u5c0f\u5206\u7c7b\u8868',
                'db_table': 't_smallcategory',
                'managed': True,
                'verbose_name_plural': '\u5c0f\u5206\u7c7b\u8868',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_name', models.CharField(max_length=20, verbose_name='\u6b21\u5206\u7c7b\u540d')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': '\u6b21\u5206\u7c7b\u8868',
                'db_table': 't_subcategory',
                'managed': True,
                'verbose_name_plural': '\u6b21\u5206\u7c7b\u8868',
            },
        ),
        migrations.RemoveField(
            model_name='course',
            name='type',
        ),
        migrations.DeleteModel(
            name='CourseType',
        ),
        migrations.AddField(
            model_name='detailcategory',
            name='main_category',
            field=models.ForeignKey(related_name='detail_main', verbose_name='\u4e3b\u5206\u7c7b\u540d', to='index.MainCategory'),
        ),
        migrations.AddField(
            model_name='detailcategory',
            name='small_category',
            field=models.ForeignKey(related_name='detail_small', verbose_name='\u5c0f\u5206\u7c7b\u540d', to='index.SmallCategory'),
        ),
        migrations.AddField(
            model_name='detailcategory',
            name='sub_category',
            field=models.ForeignKey(related_name='detail_sub', verbose_name='\u6b21\u5206\u7c7b\u540d', to='index.SubCategory'),
        ),
        migrations.AddField(
            model_name='coursecategory',
            name='course',
            field=models.ForeignKey(related_name='course_course', verbose_name='\u8bfe\u7a0b', to='index.Course'),
        ),
        migrations.AddField(
            model_name='coursecategory',
            name='detail_category',
            field=models.ForeignKey(related_name='course_detail', verbose_name='\u8be6\u7ec6\u5206\u7c7b', to='index.DetailCategory'),
        ),
    ]
