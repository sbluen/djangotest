from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

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



