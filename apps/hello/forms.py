# -*- coding: utf-8 -*-
from django import forms
from apps.hello.models import Person
from apps.hello.widgets import DatePickerWidget


class PersonEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PersonEditForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['photo', 'date_of_birth']:
                self.fields[field].widget.attrs['class'] = 'form-control'
                if field in ['bio', 'other']:
                    self.fields[field].widget.attrs['rows'] = '3'

    class Meta:
        model = Person
        widgets = {
            'date_of_birth': DatePickerWidget(
                attrs={'class': 'form-control datepicker-here',
                       'readonly': 'readonly'}),
            'photo': forms.FileInput()
        }
