# -*- coding: utf-8 -*-
import json
from django.test import TestCase
from django.core.urlresolvers import reverse
from factories import RequestFactory
from apps.hello.models import Request


class RequestViewTests(TestCase):

    def test_available_links(self):
        """
        is invalid links (test_page) unavailable, and valid is available
        """
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get('test_page')
        self.assertEqual(response.status_code, 404)

    def test_template_mid(self):
        """
        is requests items show in 'requests' page
        """
        request = RequestFactory(file_path='/requests/')
        response = self.client.get(reverse('requests'))
        self.assertContains(response, request.file_path, 1)

    def test_show_limit_in_page(self):
        """
        is on page display only 10 requests
        """
        for i in range(6):
            RequestFactory(file_path='/')
            RequestFactory(file_path='/requests/')
        response = self.client.get(reverse('requests'))
        self.assertContains(response, '<td>GET</td>', 10)

    def test_requests_order(self):
        """
        is requests in right order
        """
        RequestFactory(file_path='/')
        RequestFactory(file_path='/requests/')
        requests = Request.objects.all()[:10]
        response = self.client.get(reverse('requests'))
        data = response.context['requests'][0]['date_time']
        self.assertTrue(data < str(requests[1].date_time))

    def test_last_request(self):
        """
        is last request render in page
        """
        for i in range(8):
            RequestFactory(file_path='/')
            RequestFactory(file_path='/requests/')
        req_from_db = [r.as_dict() for r in Request.objects.all()[:10]]
        response = self.client.get(reverse('requests'))
        self.assertListEqual(req_from_db, response.context['requests'])

    def test_is_ajax_return_len_json(self):
        """
        is ajax return len json
        """
        for i in range(3):
            RequestFactory(file_path='/')
            RequestFactory(file_path='/requests/')
        response = self.client.get(
            reverse('requests_count'),
            {"id": "1"},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        json_response = json.loads(response.content)
        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['len'], 6)

    def test_is_ajax_return_object_json(self):
        """
        is ajax return object json
        """
        for i in range(3):
            RequestFactory(file_path='/')
            RequestFactory(file_path='/requests/')
        response = self.client.get(
            reverse('priority_requests'),
            data={'priority': '1', 'sort': '-date_time'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        json_response = json.loads(response.content)
        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['requests'][0]['status'], '200')
        self.assertEqual(
            json_response['requests'][0]['ver_protocol'], 'HTTP/1.1')
        self.assertEqual(json_response['requests'][0]['method'], 'GET')
        self.assertEqual(json_response['requests'][0]['content'], '1000')
        self.assertEqual(
            json_response['requests'][0]['file_path'], '/requests/')


class RequestMiddlewareTests(TestCase):

    def test_requests_write_in_db(self):
        """
        is requests write in db
        """
        requests = Request.objects.all()
        self.assertEqual(requests.count(), 0)
        for i in range(5):
            self.client.get(reverse('index'))
            self.client.get(reverse('requests'))
        requests = Request.objects.all()
        self.assertEqual(requests.count(), 10)
