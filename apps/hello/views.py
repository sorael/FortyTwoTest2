# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.hello.models import Person


def view_contact(request):
    contact = Person.objects.first()
    return render(request, 'hello/index.html', {'contact': contact})


def view_requests(request):
    requests = [{'date_time': '2016-02-05 10:02:43',
                 'method': 'GET',
                 'file_path': '/',
                 'ver_protocol': 'HTTP/1.1',
                 'status': '200',
                 'content': '1508'}]
    return render(request, 'hello/requests.html', {'requests': requests * 10})
