from django.contrib import admin

from forum.models import Forum
admin.site.register(Forum)

from forum.models import Topic
admin.site.register(Topic)

from forum.models import Post
admin.site.register(Post)
