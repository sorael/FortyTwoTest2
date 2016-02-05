# -*- coding: utf-8 -*-
from django.shortcuts import render


def view_contact(request):
    contact = {
        'first_name': 'Anatolii',
        'last_name': 'Soroka',
        'date_of_birth': '1981.02.21',
        'bio': 'Junior Python/Django',
        'email': 'sorokaanatolii@gmail.com',
        'jabber': 'a-soroka@khavr.com',
        'skype': 's-sorael',
        'other': 'Mobile phone: +380684021358'
    }
    return render(request, 'hello/index.html', {'contact': contact})
