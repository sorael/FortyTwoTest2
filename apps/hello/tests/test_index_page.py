# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


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
