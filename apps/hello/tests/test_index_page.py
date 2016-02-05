# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Person


class IndexPageTests(TestCase):

    def test_index(self):
        """
        Is index page is available
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_html(self):
        """
        Is html shows
        """
        response = self.client.get(reverse('index'))
        self.assertContains(response, '<div>Soroka</div>')
        self.assertContains(response, '<div>Jabber: a-soroka@khavr.com</div>')
        self.assertContains(
            response,
            '<h1 class="text-center">42 Coffee Cups Test Assignment</h1>')

    def test_data_index(self):
        """
        Is data from db is show on the index page
        """
        response = self.client.get(reverse('index'))
        contacts = Person.objects.all()
        self.assertEqual(contacts.count(), 1)
        contact = Person.objects.first()
        self.assertContains(response, contact.first_name, 1)
        self.assertContains(response, contact.last_name, 1)
        self.assertContains(response, contact.bio, 1)
        self.assertContains(response, contact.email, 1)
        self.assertContains(response, contact.jabber, 1)
        self.assertContains(response, contact.skype, 1)
        self.assertContains(response, contact.other, 1)
        self.assertTrue(contact.id == 1)