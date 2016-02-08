# -*- coding: utf-8 -*-
from django import forms
from apps.hello.models import Person


class PersonEditForm(forms.ModelForm):

    class Meta:
        model = Person
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            "bio": forms.Textarea(attrs={'class': 'form-control',
                                         'rows': '3'}),
            "date_of_birth": forms.DateInput(attrs={'class': 'form-control'}),
            "email": forms.TextInput(attrs={'class': 'form-control'}),
            "jabber": forms.TextInput(attrs={'class': 'form-control'}),
            "skype": forms.TextInput(attrs={'class': 'form-control'}),
            "other": forms.Textarea(attrs={'class': 'form-control',
                                           'rows': '3'}),
            "photo": forms.FileInput()
        }
