# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',
    url(r'^$', 'apps.hello.views.view_contact', name='index'),
    url(r'^requests/', 'apps.hello.views.view_requests', name='requests'),
    url(r'^requests_count/', 'apps.hello.views.requests_count',
        name='requests_count'),
    url(r'^edit_person/', 'apps.hello.views.edit_person', name='edit_person'),
)
