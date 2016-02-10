# -*- coding: utf-8 -*-
from io import BytesIO
from datetime import datetime
from django.test import TestCase
from django.db.models import get_models
from django.core.management import call_command
from django.conf import settings


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
        is stderr output saves in file with name current date
        """
        file_name = '%s-0%s-%s.dat' % (datetime.now().year,
                                       datetime.now().month,
                                       datetime.now().day)
        file_path = settings.BASE_DIR + '/' + file_name
        with open(file_name, 'w') as err:
            call_command('view_models', stderr=err)
        with open(file_path, 'r') as f:
            for line in f:
                self.assertTrue(line.startswith('error:'))
