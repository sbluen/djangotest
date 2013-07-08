"""This is the root routing module. It branches out into other routing modules."""

try:
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
    
except ImportError:
    #If we are here, we are doing documentation and we don't want interference 
    #from errors.
    pass    