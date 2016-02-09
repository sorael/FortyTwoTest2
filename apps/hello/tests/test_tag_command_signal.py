# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template import Template, Context
from apps.hello.models import Person


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
        is tag with right parameters render right string
        """
        html = '{% load edit_link %}{% edit_link obj %}'
        person = Person.objects.first()
        template = Template(html).render(Context({'obj': person}))
        self.assertEqual(template, get_edit_link())
