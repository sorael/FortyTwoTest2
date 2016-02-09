# -*- coding: utf-8 -*-
from io import BytesIO
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.db.models import get_models
from django.core.management import call_command
from apps.hello.models import Person, Request, LoggingOperation


def get_edit_link():
    person = Person.objects.first()
    return reverse('admin:%s_%s_change' % (person._meta.app_label,
                                           person._meta.module_name),
                   args=(person.id,))


class EditLinkTagTests(TestCase):

    def test_available_tag(self):
        """
        is edit link presence in index page
        """
        response = self.client.get(reverse('index'))
        self.assertNotContains(response, get_edit_link())
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('index'))
        self.assertContains(response, get_edit_link(), 1)

    def test_tag_template(self):
        """
        is tag with valid parameter render right string
        """
        html = '{% load edit_link %}{% edit_link obj %}'
        person = Person.objects.first()
        template = Template(html).render(Context({'obj': person}))
        self.assertEqual(template, get_edit_link())


class CommandOutputTests(TestCase):

    def test_command_output(self):
        """
        test output command
        """
        out = BytesIO()
        err = BytesIO()
        call_command('view_models', stdout=out, stderr=err)
        out = out.getvalue()
        err = err.getvalue()
        for model in get_models():
            out_ = 'Name: %s. Objects count: %s.' %\
                   (model.__name__, model.objects.count())
            self.assertIn('error: ' + out_, err)
            self.assertIn(out_, out)


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
