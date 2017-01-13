#-*-coding:UTF-8-*-
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import NoticeArticle

def notification_show(reqeust,id):
    notice_article = NoticeArticle.objects.get(id=id)
    if notice_article is None:
        return Http404('not found')
    context = dict(notification = notice_article,
                   category_name = NoticeArticle.CATEGORY_CHOICES[int(notice_article.category)][1])
    return render(reqeust, 'notifications_management/show.html', context)

def notification_home(request):
    '''
    显示通知列表，按照分类显示 0 和 1 两个分类列表
    :param request:
    :return:
    '''
    object_list0 = NoticeArticle.objects.filter(category=0).order_by('-create_at')
    object_list1 = NoticeArticle.objects.filter(category=1).order_by('-create_at')
    # Defined page size
    paginator0 = Paginator(object_list0, 5)
    paginator1 = Paginator(object_list1, 5)
    page0 = int(request.GET.get('page0',1))
    page1 = int(request.GET.get('page1',1))
    try:
        # Located page
        articles0 = paginator0.page(page0)
        articles1 = paginator1.page(page1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles0 = paginator0.page(1)
        articles1 = paginator1.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles0 = paginator0.page(paginator0.num_pages)
        articles1 = paginator1.page(paginator1.num_pages)
    # 显示分类名称
    context = dict(object_list0=articles0, object_list1 = articles1
                   )
    return render(request, 'notifications_management/home.html', context)