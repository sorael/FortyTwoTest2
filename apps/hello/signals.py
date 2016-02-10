# -*- coding: utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from apps.hello.models import LoggingOperation


@receiver(post_save)
def save_signal(sender, created, **kwargs):
    if sender.__name__ == 'LoggingOperation':
        return
    operation_type = 'create' if created else 'update'
    LoggingOperation.objects.create(
        model_name=sender.__name__,
        operation_type=operation_type)


@receiver(post_delete)
def delete_signal(sender, **kwargs):
    operation_type = 'delete'
    if sender.__name__ != 'LoggingOperation':
        LoggingOperation.objects.create(
            model_name=sender.__name__,
            operation_type=operation_type)
