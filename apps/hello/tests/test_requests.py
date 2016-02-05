# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class RequestViewTests(TestCase):

    def test_available_links(self):
        """
        is invalid links (test_page) unavailable, and valid is available
        """
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)

    def test_requests_html(self):
        """
        is html shows
        """
        response = self.client.get(reverse('requests'))
        self.assertContains(response, '<td>GET</td>', 10)
        self.assertContains(response, '<td>HTTP/1.1</td>', 10)
