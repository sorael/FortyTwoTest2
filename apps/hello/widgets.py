# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.storage import staticfiles_storage


class DatePickerWidget(forms.DateInput):
    class Media:
        css = {
            'all': (staticfiles_storage.url('css/datepicker.min.css'),)
        }
        js = (
            settings.STATIC_URL + 'js/datepicker.min.js',
            settings.STATIC_URL + 'js/edit_person.js',
        )

    def __init__(self, attrs=None):
        super(DatePickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(DatePickerWidget, self).render(name, value, attrs)
        return rendered + mark_safe(u'''
            <script>
                $('#id_%s').datepicker({
                    dateFormat: 'yyyy-mm-dd',
                    position: 'bottom left',
                });
            </script>
            ''' % name)
