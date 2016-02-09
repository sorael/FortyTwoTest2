# -*- coding: utf-8 -*-
from django import template
from django.core import urlresolvers


register = template.Library()


def edit_link(obj):
    return urlresolvers.reverse("admin:%s_%s_change" %
                                (obj._meta.app_label, obj._meta.module_name),
                                args=(obj.id,))

register.simple_tag(edit_link)
