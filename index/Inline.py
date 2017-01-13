# coding:utf-8
from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline
from index.models import SubCategory, SmallCategory

# class SubCategoryInline(admin.TabularInline):
#     model = SubCategory
#     extra = 1
#
# class SmallCategoryInline(admin.TabularInline):
#     model = SmallCategory
#     extra = 1
# use nest-inline
class SmallCategoryInline(NestedTabularInline):
    model = SmallCategory
    extra = 1
    verbose_name = u''
    verbose_name_plural = u''

class SubCategoryInline(NestedStackedInline):
    model = SubCategory
    inlines = [SmallCategoryInline, ]
    extra = 1
    verbose_name = u'添加主分类和小分类'
    verbose_name_plural = u''

# use super-inlin

