# -*- coding: utf-8 -*-
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=250)
    other = models.TextField()
