# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.hello.models import Person, Request
from apps.hello.forms import PersonEditForm
import apps.hello.signals  # noqa


def view_contact(request):
    contact = Person.objects.first()
    return render(request, 'hello/index.html', {'contact': contact})


def requests_count(request):
    last_id = int(request.GET['id'])
    if request.is_ajax():
        new_requests = Request.objects.filter(id__gte=last_id)
        return HttpResponse(json.dumps({'len': len(new_requests)}),
                            content_type="application/json")


def priority_requests(request):
    if request.is_ajax():
        priority = request.GET['priority']
        sorting = request.GET['sort']
        if priority == 'all':
            requests = Request.objects.order_by(sorting)[:10]
        elif 0 > int(priority[-1]) > 3:
            return HttpResponse(json.dumps({'success': 'false'}),
                                content_type='application/json')
        else:
            requests = Request.objects.filter(
                priority=int(priority[-1])).order_by(sorting)[:10]
        req_json = [r.as_dict() for r in requests]
        response_data = {'requests': req_json, 'success': 'true'}
        return HttpResponse(json.dumps(response_data),
                            content_type='application/json')
    requests = Request.objects.all()[:10]
    req_json = [r.as_dict() for r in requests]
    response_data = {'requests': req_json}
    return render(request, 'hello/requests.html', response_data)


def change_priority(request):
    request_count = Request.objects.all().count()
    if request.is_ajax():
        request_id = int(request.GET['request_id'])
        priority = int(request.GET['priority'])
        if (3 >= priority >= 1) and (request_count >= request_id >= 1):
            Request.objects.filter(id=request_id).update(priority=priority)
            return HttpResponse(json.dumps({'success': 'true'}),
                                content_type='application/json')
        else:
            return HttpResponse(json.dumps({'success': 'false'}),
                                content_type='application/json')


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
