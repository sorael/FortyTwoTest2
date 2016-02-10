# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Person, Request, LoggingOperation


class SignalProcessorTests(TestCase):

    def test_logging_operation_add(self):
        """
        test adding information to LoggingOperation
        """
        LoggingOperation.objects.all().delete()
        self.assertEqual(LoggingOperation.objects.count(), 0)
        person = Person.objects.create(first_name='test',
                                       last_name='last_name',
                                       email='email@email.com',
                                       jabber='jabber@jabber.com',
                                       skype='skype',
                                       other='other',
                                       bio='bio',
                                       date_of_birth='1990-10-09')
        self.assertEqual(LoggingOperation.objects.count(), 1)
        person.first_name = 'another test'
        person.save()
        self.assertEqual(LoggingOperation.objects.count(), 2)
        person.delete()
        self.assertEqual(LoggingOperation.objects.count(), 3)
        self.client.get(reverse('index'))
        self.assertEqual(LoggingOperation.objects.count(), 4)

    def test_logging_operation_info(self):
        """
        test content of add row
        """
        LoggingOperation.objects.all().delete()
        person = Person.objects.create(first_name='test',
                                       last_name='last_name',
                                       email='email@email.com',
                                       jabber='jabber@jabber.com',
                                       skype='skype',
                                       other='other',
                                       bio='bio',
                                       date_of_birth='1990-10-09')
        log = LoggingOperation.objects.last()
        self.assertEqual(log.model_name, person.__class__.__name__)
        person.first_name = 'name2'
        person.save()
        log = LoggingOperation.objects.last()
        self.assertEqual(log.model_name, person.__class__.__name__)
        self.assertEqual(log.operation_type, 'update')
        person.delete()
        log = LoggingOperation.objects.last()
        self.assertEqual(log.model_name, person.__class__.__name__)
        self.assertEqual(log.operation_type, 'delete')
        self.client.get(reverse('index'))
        request = Request.objects.last()
        log = LoggingOperation.objects.last()
        self.assertEqual(log.model_name, request.__class__.__name__)
        self.assertEqual(log.operation_type, 'create')
