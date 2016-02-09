# -*- coding: utf-8 -*-
from django.db import models
from PIL import Image


class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=250)
    other = models.TextField()
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)
        if self.photo:
            image = Image.open(self.photo)
            image.thumbnail((200, 200), Image.ANTIALIAS)
            image.save(self.photo.path, 'JPEG', quality=80)


class Request(models.Model):
    date_time = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=7)
    file_path = models.CharField(max_length=250)
    ver_protocol = models.CharField(max_length=10)
    status = models.CharField(max_length=3)
    content = models.CharField(max_length=8)

    def as_dict(self):
        return {'date_time': str(self.date_time)[:19],
                'method': self.method,
                'file_path': self.file_path,
                'ver_protocol': self.ver_protocol,
                'status': self.status,
                'content': self.content,
                'id': self.id
                }

    class Meta:
        ordering = ['-date_time']


class LoggingOperation(models.Model):
    model_name = models.CharField(max_length=100)
    operation_type = models.CharField(max_length=6)
    operation_date = models.DateTimeField(auto_now_add=True)
