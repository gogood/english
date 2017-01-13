# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book_name', models.CharField(max_length=100, verbose_name='\u6559\u6750\u540d\u5b57')),
                ('description', models.CharField(max_length=300, verbose_name='\u6559\u6750\u63cf\u8ff0')),
                ('money', models.IntegerField(verbose_name='\u91d1\u989d')),
                ('special', models.CharField(max_length=500, verbose_name='\u6559\u6750\u7279\u8272')),
            ],
            options={
                'ordering': ['book_name'],
                'verbose_name': '\u6559\u6750',
                'db_table': 't_book',
                'managed': True,
                'verbose_name_plural': '\u6559\u6750',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=100, verbose_name='\u8bfe\u7a0b\u7c7b\u578b\u540d')),
                ('description', models.CharField(max_length=1000, verbose_name='\u8bfe\u7a0b\u63cf\u8ff0')),
                ('target', models.CharField(max_length=100, verbose_name='\u8bfe\u7a0b\u9884\u8ba1\u76ee\u6807')),
                ('setting', models.CharField(max_length=1000, verbose_name='\u8bfe\u7a0b\u8bbe\u7f6e')),
            ],
            options={
                'ordering': ['course_name'],
                'verbose_name': '\u8bfe\u7a0b\u8868',
                'db_table': 't_course',
                'managed': True,
                'verbose_name_plural': '\u8bfe\u7a0b\u8868',
            },
        ),
        migrations.CreateModel(
            name='CourseType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=100, verbose_name='\u8bfe\u7a0b\u7c7b\u578b\u540d')),
            ],
            options={
                'ordering': ['type_name'],
                'verbose_name': '\u8bfe\u7a0b\u7c7b\u578b\u8868',
                'db_table': 't_coursetype',
                'managed': True,
                'verbose_name_plural': '\u8bfe\u7a0b\u7c7b\u578b\u8868',
            },
        ),
        migrations.CreateModel(
            name='DocSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doc_name', models.CharField(max_length=100, verbose_name='\u6587\u6863\u540d')),
                ('content', models.FileField(upload_to=b'static/doc', verbose_name='\u6587\u6863\u5185\u5bb9')),
            ],
            options={
                'ordering': ['doc_name'],
                'verbose_name': '\u6587\u6863\u8d44\u6599\u8868',
                'db_table': 't_doc',
                'managed': True,
                'verbose_name_plural': '\u6587\u6863\u8d44\u6599\u8868',
            },
        ),
        migrations.CreateModel(
            name='DocType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_name', models.CharField(max_length=100, verbose_name='\u6587\u6863\u7c7b\u578b\u540d')),
            ],
            options={
                'ordering': ['type_name'],
                'verbose_name': '\u6587\u6863\u7c7b\u578b\u8868',
                'db_table': 't_doctype',
                'managed': True,
                'verbose_name_plural': '\u6587\u6863\u7c7b\u578b\u8868',
            },
        ),
        migrations.AddField(
            model_name='docsite',
            name='course',
            field=models.ForeignKey(related_name='course', verbose_name='\u8bfe\u7a0b', to='index.DocType'),
        ),
        migrations.AddField(
            model_name='docsite',
            name='type',
            field=models.ForeignKey(related_name='doc_type', verbose_name='\u6587\u6863\u7c7b\u578b', to='index.DocType'),
        ),
        migrations.AddField(
            model_name='course',
            name='type',
            field=models.ForeignKey(related_name='course', verbose_name='\u8bfe\u7a0b\u7c7b\u578b', to='index.CourseType'),
        ),
        migrations.AddField(
            model_name='book',
            name='course',
            field=models.ForeignKey(related_name='course', verbose_name='\u8bfe\u7a0b', to='index.Course'),
        ),
    ]
