# -*- coding: utf-8 -*-
import os
import subprocess
from io import BytesIO
from datetime import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.db.models import get_models
from django.core.management import call_command
from django.conf import settings
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

    def test_file_stderr_save(self):
        """
        is bash script works and saves all stderr output
        in file with current date name
        """
        script_file = settings.BASE_DIR + "/err_to_file.sh"
        os.chmod(script_file, 0555)
        subprocess.call(script_file)
        file_name = '%s-0%s-0%s.dat' % (datetime.now().year,
                                        datetime.now().month,
                                        datetime.now().day)
        file_path = settings.BASE_DIR + '/' + file_name
        with open(file_path, 'r') as f:
            for line in f:
                self.assertTrue(line.startswith('error: Name:'))
