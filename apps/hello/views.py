# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.hello.models import Person, Request
from apps.hello.forms import PersonEditForm


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


@login_required
def edit_person(request):
    contact = Person.objects.first()
    form = PersonEditForm(instance=contact)
    if request.POST and request.is_ajax():
        form = PersonEditForm(request.POST, request.FILES, instance=contact)
        response = {}
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            response['photo'] = str(contact.photo)
            response['success'] = 'true'
        else:
            if form.errors:
                errs = {}
                for error in form.errors:
                    e = form.errors[error]
                    errs[error] = unicode(e)
                response['success'] = 'false'
                response['errors'] = errs
        return HttpResponse(json.dumps(response),
                            content_type='application/json')
    return render(request, 'hello/edit_person.html',
                  {'form': form, 'contact': contact})
