import factory
from django.utils import timezone
from apps.hello.models import Request


class RequestFactory(factory.django.DjangoModelFactory):

    FACTORY_FOR = Request
    date_time = timezone.now()
    method = 'GET'
    file_path = '/'
    ver_protocol = 'HTTP/1.1'
    status = '200'
    content = '1000'
