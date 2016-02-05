# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.hello.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "date_of_birth", "bio",
                    "email", "jabber", "skype", "other"]

admin.site.register(Person, PersonAdmin)
