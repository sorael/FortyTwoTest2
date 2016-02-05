# -*- coding: utf-8 -*-
from django.shortcuts import render
from apps.hello.models import Person


def view_contact(request):
    contact = Person.objects.first()
    return render(request, 'hello/index.html', {'contact': contact})


def view_requests(request):
    return render(request, 'hello/requests.html')
