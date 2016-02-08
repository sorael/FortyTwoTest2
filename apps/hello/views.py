# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse
from apps.hello.models import Person, Request


def view_contact(request):
    contact = Person.objects.first()
    return render(request, 'hello/index.html', {'contact': contact})


def requests_count(request):
    last_id = int(request.GET['id'])
    if request.is_ajax():
        new_requests = Request.objects.filter(id__gte=last_id)
        response_data = {'len': len(new_requests)}
        return HttpResponse(json.dumps(response_data),
                            content_type="application/json")


def view_requests(request):
    requests = Request.objects.all()[:10]
    req_json = [r.as_dict() for r in requests]
    response_data = {'requests': req_json}
    if request.is_ajax():
        return HttpResponse(json.dumps(response_data),
                            content_type="application/json")
    return render(request, 'hello/requests.html', response_data)


def edit_person(request):
    contact = {
        'first_name': 'Anatolii',
        'last_name': 'Soroka',
        'date_of_birth': '1981-02-21',
        'bio': 'Junior Python/Django',
        'email': 'sorokaanatolii@gmail.com',
        'jabber': 'a-soroka@khavr.com',
        'skype': 's-sorael',
        'other': 'Mobile phone: +380684021358'
    }
    return render(request, 'hello/edit_person.html', {'contact': contact})
