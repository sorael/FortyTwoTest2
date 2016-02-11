# -*- coding: utf-8 -*-
import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from apps.hello.tests.factories import RequestFactory
from apps.hello.models import Request


class TestRequestPriority(TestCase):

    def test_change_request_invalid_priority(self):
        """
        test for change request with invalid priority
        """
        RequestFactory()
        response = self.client.get(
            reverse('change_priority'),
            {'priority': '51', 'request_id': '1'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['success'], 'false')

    def test_change_request_invalid_id(self):
        """
        test for change request with invalid id
        """
        RequestFactory()
        response = self.client.get(
            reverse('change_priority'),
            {'priority': '2', 'request_id': '99'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['success'], 'false')

    def test_change_request_valid_data(self):
        """
        test for  change request with valid data
        """
        RequestFactory()
        response = self.client.get(
            reverse('change_priority'),
            {'priority': '3', 'request_id': '1'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['success'], 'true')
        self.assertEqual(Request.objects.get(id=1).priority, 3)


class TestRequestSort(TestCase):

    def test_sorting_asc(self):
        """
        is sorting change ascending
        """
        for i in range(0, 10):
            RequestFactory()
        requests_db = Request.objects.order_by('date_time')[:10]
        requests_dict = [r.as_dict() for r in requests_db]
        response = self.client.get(reverse('priority_requests'),
                                   {'sort': 'date_time', 'priority': 'all'},
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        requests = json.loads(response.content)
        self.assertEqual(requests['requests'], requests_dict)

    def test_sorting_desc(self):
        """
        is sorting change descending
        """
        for i in range(0, 10):
            RequestFactory()
        requests_db = Request.objects.order_by('-date_time')[:10]
        requests_dict = [r.as_dict() for r in requests_db]
        response = self.client.get(reverse('priority_requests'),
                                   {'sort': '-date_time', 'priority': 'all'},
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        requests = json.loads(response.content)
        self.assertEqual(requests['requests'], requests_dict)
