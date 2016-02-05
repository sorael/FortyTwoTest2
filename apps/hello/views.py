# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.hello.models import Person, Request


def view_contact(request):
    contact = Person.objects.first()
    return render(request, 'hello/index.html', {'contact': contact})


def view_requests(request):
    requests = Request.objects.all()[:10]
    req_json = [r.as_dict() for r in requests]
    response_data = {'requests': req_json}
    return render(request, 'hello/requests.html', response_data)
