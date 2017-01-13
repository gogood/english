# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
import views

urlpatterns = [
    # 报表
    url(r'^notification/show/(\d+)/', views.notification_show, name='notification_show'),
    url(r'^notification/home/', views.notification_home, name='notification_home'),
]
