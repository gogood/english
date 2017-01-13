"""edu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from index import views

urlpatterns = [
    # app url
    url(r'^$', views.index, name='index'), # main page
    url(r'^course/$', views.course, name='course'), # course page
    url(r'^register/$',views.register, name='register'), # register page
    url(r'^forget_password/$', views.forget_password, name='forget_password'), # forget_password
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^user_center/$', views.user_center, name='user_center'),
    url(r'^apply/$', views.apply, name='apply'),
    url(r'^user/$', views.user, name='user'),
    url(r'^course_detail/$', views.course_detail, name='course_detail'),

    # api
    url(r'^api_course/$', views.api_course, name='api_course'), # course main page api
    url(r'^api_course_category/$', views.api_course_category, name='api_course_category'), # course category search
    url(r'^api_course_search/$', views.api_course_search, name='api_course_search'), # course search

    url(r'^register_message_validate/$', views.register_message_validate, name='register_message_validate'), # use baidudayu api will get mobile message,when you register or forget password
    url(r'^api_register/$', views.api_register, name='api_register'), # when you register ,you will use it
    url(r'api_apply/$', views.api_apply, name='api_apply'), # when you free apply a course
    url(r'^api_mobile_is_exist/$', views.api_mobile_is_exist, name='api_mobile_is_exist'),# validate the mobile is exit in database
    url(r'^api_forget_password/$', views.api_forget_password, name='api_forget_password'), # when you forget you password
    url(r'^api_login/$', views.api_login, name='api_login'),

    # url(r'^image/imageUp/$', views.image_up, name='image_up'),

    # test
    url(r'^test/$', views.test, name='test')
]
