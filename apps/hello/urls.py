# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth import views


urlpatterns = patterns(
    '',
    url(r'^$', 'apps.hello.views.view_contact', name='index'),
    url(r'^requests/', 'apps.hello.views.priority_requests', name='requests'),
    url(r'^requests_count/', 'apps.hello.views.requests_count',
        name='requests_count'),
    url(r'^priority_requests/', 'apps.hello.views.priority_requests',
        name='priority_requests'),
    url(r'^change_priority/', 'apps.hello.views.change_priority',
        name='change_priority'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, {'next_page': '/'}, name='logout'),
    url(r'^edit_person/', 'apps.hello.views.edit_person', name='edit_person'),
)
