# -*- coding: utf-8 -*-
from django.shortcuts import render


def view_contact(request):
    return render(request, 'hello/index.html')
