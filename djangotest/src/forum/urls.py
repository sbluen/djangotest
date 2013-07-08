"""This is the forum routing module."""

try:
    from django.conf.urls import patterns, url
    urlpatterns = patterns('forum.views',
    
        url(r'^forum/$', 'forum_list', name='forum-list'),
        url(r'^forum/(?P<id>\d+)/$', 'forum_details', name='forum-details'),
    #     url(r'^forum/(?P<id>\d+)/delete/$', 'forum_delete', name='forum-delete'),
    
    #     url(r'^post/$', 'post_list', name='post-list'),
        url(r'^post/(?P<id>\d+)/$', 'post_details', name='post-details'),
    #     url(r'^post/(?P<id>\d+)/delete/$', 'post_delete', name='post-delete'),
    
    #     url(r'^topic/$', 'topic_list', name='topic-list'),
        url(r'^topic/(?P<id>\d+)/$', 'topic_details', name='topic-details'),
    #     url(r'^topic/(?P<id>\d+)/delete/$', 'topic_delete', name='topic-delete'),
        url(r'^$', 'forum_list', name='forum-list'),
        #url(r'^/(?P<id>\d+)/$', 'forum_details', name='forum-details'),
    #     url(r'^/(?P<id>\d+)/delete/$', 'forum_delete', name='forum-delete'),
    )
except ImportError:
    #If we are here, we are doing documentation and we don't want interference 
    #from errors
    pass    