from django.db import models

# Create your models here.

class Forum(models.Model):
    
    name = models.CharField(max_length=255, null=True, blank=True)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

from django.contrib.auth.models import User, Group
from forum.models import Forum
class Topic(models.Model):
    
    created_by = models.ForeignKey(User, null=True, blank=True)

    title = models.CharField(max_length=255, null=True, blank=True)

    forum = models.ForeignKey(Forum, null=True, blank=True)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
    
from forum.models import Topic
class Post(models.Model):
    
    title = models.CharField(max_length=255, null=True, blank=True)

    body = models.TextField(null=True, blank=True)

    created_by = models.ForeignKey(User, null=True, blank=True)

    topic = models.ForeignKey(Topic, null=True, blank=True)

    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
        
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
