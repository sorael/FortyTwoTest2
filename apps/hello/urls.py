# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'apps.hello.views.view_contact', name='index'),
    url(r'^requests/', 'apps.hello.views.view_requests', name='requests'),
)
