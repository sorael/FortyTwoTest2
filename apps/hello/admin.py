# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.hello.models import Person, Request, LoggingOperation


class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "date_of_birth", "bio",
                    "email", "jabber", "skype", "other"]


class RequestAdmin(admin.ModelAdmin):
    list_display = ["date_time", "method", "file_path",
                    "ver_protocol", "status", "content"]


class LoggingOperationAdmin(admin.ModelAdmin):
    list_display = ["model_name", "operation_type", "operation_date"]


admin.site.register(Person, PersonAdmin)
admin.site.register(Request, RequestAdmin)
admin.site.register(LoggingOperation, LoggingOperationAdmin)
