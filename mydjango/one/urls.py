from django.conf.urls import patterns, url

from one import views


urlpatterns = patterns('',
    url(r'^$', views.hello, name='index')
)