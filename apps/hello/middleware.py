# -*- coding: utf-8 -*-
from apps.hello.models import Request


class RequestsMiddleware(object):

    def process_response(self, request, response):
        if request.path not in ['/priority_requests/', '/requests_count/']:
            Request.objects.create(
                method=request.META['REQUEST_METHOD'],
                file_path=request.path,
                ver_protocol=request.META['SERVER_PROTOCOL'],
                status=response.status_code,
                content=len(response.content))
        return response
