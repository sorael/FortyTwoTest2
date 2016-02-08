# -*- coding: utf-8 -*-
from PIL import Image
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.hello.models import Person
from apps.hello.edit_form import PersonEditForm
from io import BytesIO


def create_img():
    image = Image.new("RGB", (500, 250), (30, 60, 90))
    output = BytesIO()
    image.save(output, 'PNG')
    output.name = 'img_for_test.png'
    output.seek(0)
    return output


def clean_photo():
    Person.objects.first().photo.delete()


class EditPersonFormTests(TestCase):

    def tearDown(self):
        clean_photo()

    def test_edit_form(self):
        """
        is edit_person page is contains person data
        """
        resp = self.client.get(reverse('edit_person'))
        person = Person.objects.first()
        self.assertContains(resp, person.first_name, 1)
        self.assertContains(resp, person.last_name, 1)
        self.assertContains(resp, person.date_of_birth, 1)
        self.assertContains(resp, person.bio, 1)
        self.assertContains(resp, person.email, 1)
        self.assertContains(resp, person.jabber, 1)
        self.assertContains(resp, person.skype, 1)
        self.assertContains(resp, person.other, 1)

    def test_invalid_data_update(self):
        """
        is validation massages is display
        """
        form_data = {'date_of_birth': '1010-1010',
                     'email': 'test',
                     'jabber': 'test'}
        form = PersonEditForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn(u'Enter a valid date',
                      str(form['date_of_birth'].errors))
        self.assertIn(u'Enter a valid email address',
                      str(form['email'].errors))
        self.assertIn(u'Enter a valid email address',
                      str(form['jabber'].errors))

    def test_no_data_update(self):
        """
        is required massages is display
        """
        form = PersonEditForm(data={})
        self.assertIn(u'This field is required',
                      str(form['first_name'].errors))
        self.assertIn(u'This field is required',
                      str(form['last_name'].errors))
        self.assertIn(u'This field is required',
                      str(form['date_of_birth'].errors))
        self.assertIn(u'This field is required', str(form['email'].errors))
        self.assertIn(u'This field is required', str(form['jabber'].errors))
        self.assertIn(u'This field is required', str(form['skype'].errors))

    def test_resize_image(self):
        """
        is image save, resize
        """
        person = Person.objects.first()
        photo = create_img()
        data = {'first_name': 'first_name',
                'last_name': 'last_name',
                'date_of_birth': '1990-10-09',
                'other': 'other',
                'bio': 'bio',
                'email': 'email@email.com',
                'jabber': 'jabber@jabber.com',
                'skype': 'skype'}
        photo = SimpleUploadedFile(photo.name, photo.read())
        form = PersonEditForm(data, dict(photo=photo), instance=person)
        self.assertTrue(form.is_valid())
        form.save()
        person = Person.objects.first()
        self.assertLessEqual(person.photo.width/person.photo.height, 500/250)


class EditPersonViewTests(TestCase):

    def test_default_image_in_contact_edit_page(self):
        """
        is default image in contact edit page
        """
        response = self.client.get(reverse('edit_person'))
        self.assertIn('/static/img/img.png', response.content)
