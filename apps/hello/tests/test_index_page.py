# -*- coding: utf-8 -*-
import os.path
import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.models import Person
from fortytwo_test_task.settings.common import BASE_DIR


class IndexPageTests(TestCase):
    fixture = os.path.join(BASE_DIR, 'apps/hello/fixtures/initial_data.json')

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
        self.assertIn(
            '<h1 class="text-center">42 Coffee Cups Test Assignment</h1>',
            response.content)

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

    def test_render_unicode(self):
        """
        Is unicode data render correctly in page
        """
        contact = Person.objects.first()
        contact.first_name = 'Анатолий'
        contact.save()
        response = self.client.get(reverse('index'))
        self.assertIn('Анатолий', response.content)

    def test_admin(self):
        """
        is admin page is available
        """
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 200)

    def test_admin_login(self):
        """
        is admin can login
        """
        admin = {'name': 'admin',
                 'password': 'admin'}
        response = self.client.post(reverse('admin:index'), admin)
        self.assertEqual(response.status_code, 200)

    def test_empty_database(self):
        """
        is message is show when db is empty
        """
        contacts = Person.objects.all()
        contacts.delete()
        response = self.client.get(reverse('index'))
        self.assertContains(response, 'Database is empty!')

    def test_is_data_in_fixture_equals_data_in_db(self):
        """
        is data from fixture is equals data in db
        """
        contact = Person.objects.first()
        with open(self.fixture) as f:
            target = json.load(f)
            self.assertTrue(
                contact.first_name == target[1]['fields']['first_name'])
            self.assertTrue(
                contact.last_name == target[1]['fields']['last_name'])
            self.assertTrue(contact.bio == target[1]['fields']['bio'])
            self.assertTrue(contact.email == target[1]['fields']['email'])
            self.assertTrue(contact.jabber == target[1]['fields']['jabber'])
            self.assertTrue(contact.skype == target[1]['fields']['skype'])
            self.assertTrue(contact.other == target[1]['fields']['other'])

    def test_is_data_in_fixture_equals_data_in_html(self):
        """
         is data from fixture is equals data in html
        """
        response = self.client.get(reverse('index'))
        with open(self.fixture) as f:
            target = json.load(f)
            self.assertContains(response, target[1]['fields']['first_name'])
            self.assertContains(response, target[1]['fields']['last_name'])
            self.assertContains(response, target[1]['fields']['bio'])
            self.assertContains(response, target[1]['fields']['email'])
            self.assertContains(response, target[1]['fields']['jabber'])
            self.assertContains(response, target[1]['fields']['skype'])
            self.assertContains(response, target[1]['fields']['other'])

    def test_is_bio_and_other_are_multiline(self):
        """
        is bio and other pages are multiline
        """
        response = self.client.get(reverse('index'))
        contact = Person.objects.first()
        # Other contacts
        self.assertInHTML('<div>Other contacts:</div>', response.content)
        self.assertInHTML('<p>%s</p>' % contact.other, response.content)
        # Bio
        self.assertInHTML('<div>Bio:</div>', response.content)
        self.assertInHTML('<p>%s</p>' % contact.bio, response.content)
