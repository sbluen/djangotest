from django.contrib import admin
from polls.models import Choice, Poll
from forum.models import Forum, Topic, Post

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    
admin.site.register(Poll, PollAdmin)

# class ForumAdmin(admin.ModelAdmin):
#     fields = ['id', 'name']
# admin.site.register(Forum, ForumAdmin)
# 
# class TopicAdmin(admin.ModelAdmin):
#     fields = ['id', 'title' 'forum_id']
# admin.site.register(Topic, TopicAdmin)
# 
# class PostAdmin(admin.ModelAdmin):
#     fields = ['id', 'title', 'topic_id']
# admin.site.register(Topic, TopicAdmin)

admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Post)