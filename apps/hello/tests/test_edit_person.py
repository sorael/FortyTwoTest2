# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse


class EditPersonViewTests(TestCase):

    def test_default_image_in_contact_edit_page(self):
        """
        is default image in contact edit page
        """
        response = self.client.get(reverse('edit_person'))
        self.assertIn('/static/img/img.png', response.content)

    def test_edit_form(self):
        """
        is edit_person page is contains person data
        """
        resp = self.client.get(reverse('edit_person'))
        self.assertTrue(resp.status_code == 200)
        self.assertContains(resp, 'Anatolii', 1)
        self.assertContains(resp, 'Soroka', 1)
        self.assertContains(resp, '1981-02-21', 1)
        self.assertContains(resp, 'Junior Python/Django', 1)
        self.assertContains(resp, 'sorokaanatolii@gmail.com', 1)
        self.assertContains(resp, 'a-soroka@khavr.com', 1)
        self.assertContains(resp, 's-sorael', 1)
        self.assertContains(resp, 'Mobile phone: +380684021358', 1)
