from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mydjango.views.home', name='home'),
    url(r'^one/', include('one.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
