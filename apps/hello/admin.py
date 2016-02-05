# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.hello.models import Person, Request


class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "date_of_birth", "bio",
                    "email", "jabber", "skype", "other"]


class RequestAdmin(admin.ModelAdmin):
    list_display = ["date_time", "method", "file_path",
                    "ver_protocol", "status", "content"]

admin.site.register(Person, PersonAdmin)
admin.site.register(Request, RequestAdmin)
