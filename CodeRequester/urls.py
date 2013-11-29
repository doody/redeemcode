from django.conf.urls import patterns, include, url
from CodeRequester import views


urlpatterns = patterns('',
                       url(r'^$', views.request_code, name='index'),
                       url(r'^request/', views.request_code, name='request'),
                       url(r'^verify/', views.code_verify, name='verify'),
)