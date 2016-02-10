# -*- coding: utf-8 -*-
from django import template
from django.core import urlresolvers


register = template.Library()


def edit_link(obj):
    try:
        link = 'admin:%s_%s_change' % (obj._meta.app_label,
                                       obj._meta.module_name)
    except AttributeError:
        raise Exception("edit_link tag expected an object of model")
    return urlresolvers.reverse(link, args=(obj.id,))

register.simple_tag(edit_link)
