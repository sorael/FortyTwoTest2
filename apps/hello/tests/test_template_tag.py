# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template import Template, Context
from apps.hello.models import Person
from apps.hello.templatetags.edit_link import edit_link


class EditLinkTagTests(TestCase):

    def test_available_tag(self):
        """
        is edit link presence in index page
        """
        person = Person.objects.first()
        response = self.client.get(reverse('index'))
        self.assertNotContains(response, edit_link(person))
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('index'))
        self.assertContains(response, edit_link(person), 1)

    def test_tag_template(self):
        """
        is tag with valid parameter render right string
        """
        html = '{% load edit_link %}{% edit_link obj %}'
        person = Person.objects.first()
        template = Template(html).render(Context({'obj': person}))
        self.assertEqual(template, edit_link(person))

    def test_invalid_object(self):
        """
        is exception generate if edit_link takes invalid object
        """
        self.assertRaises(Exception, edit_link, 'str')
