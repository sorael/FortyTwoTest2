# -*- coding: utf-8 -*-
import os
import subprocess
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

        """
        script_file = settings.BASE_DIR + "/err_to_file.sh"
        os.chmod(script_file, 0555)
        subprocess.call(script_file)
        file_name = '%s-0%s-%s.dat' % (datetime.now().year,
                                       datetime.now().month,
                                       datetime.now().day)
        file_path = settings.BASE_DIR + '/' + file_name
        with open(file_path, 'r') as f:
            for line in f:
                print ' '.join(line.split())
