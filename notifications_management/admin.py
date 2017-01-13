# -*-coding:UTF-8-*-
from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django_ueditor.widgets import UEditorWidget
from django import forms
from .models import NoticeArticle


class ArticleForm(forms.ModelForm):
    content = forms.CharField(label=u"内容",
                              widget=UEditorWidget(width=800, height=500,toolbars={}))


class NoticeArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

    def show_at_new_window(self, obj):
        '''
        在新窗口显示内容
        :param obj: NotificeArticle
        :return: link element
        '''
        link_str = u'<a href="{}" target="_blank">{}</a>'
        url = unicode(reverse(u'notifications_management:notification_show', args=(obj.id,)))
        return format_html(link_str, url, u'查看')

    show_at_new_window.short_description = u'查看'

    def get_readonly_fields(self, request, obj=None):
        # 做权限判断
        return (None,)

    list_display = ('show_at_new_window','title', 'create_at')
    list_filter = ('category',)

    def get_list_display_links(self, request, list_display):
        # 做权限判断
        return ('title',)
    fieldsets = [
        (None, {'classes': ('wide',), 'fields': ('title', 'create_at', 'category')}),
        (u'正文', {'classes': ('full-width',), 'fields': ('content',)})
    ]

    def has_add_permission(self, request):
        if request.user.is_superuser or request.user.groups.filter(name='Admin'):
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or request.user.groups.filter(name='Admin'):
            return True
        else :
            return False


admin.site.register(NoticeArticle, NoticeArticleAdmin)
