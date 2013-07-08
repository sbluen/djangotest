"""This is the root routing module. It branches out into other routing modules."""

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    #url(r'^forum/', include('forum.urls', namespace="forum")),
    url(r'^forum/', include('forum.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('forum.urls'))
)



