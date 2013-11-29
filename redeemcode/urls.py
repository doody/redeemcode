from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^code_req/', include('CodeRequester.urls'), name='code_req'),
                       url(r'^admin/', include(admin.site.urls)),
)
