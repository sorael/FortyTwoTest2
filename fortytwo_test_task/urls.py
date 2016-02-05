from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('apps.hello.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
