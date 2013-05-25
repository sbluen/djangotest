# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.middleware.csrf import get_token
from django_common.http import JsonResponse
from forum.models import Forum
from forum.forms import ForumForm
def forum_list(request, template='forum/list.html'):
    d = {}
    d['form'] = ForumForm()
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            item = form.save()
            return JsonResponse(data={'username': item.username, 'password': item.password, 'form': ForumForm().as_p(), 'token': get_token(request)})
        else:
            d['form'] = form
            return JsonResponse(data={'form': d['form'].as_p(), 'token': get_token(request)}, success=False)
    d['forum_list'] = Forum.objects.all()
    return render(request, template, d)

from forum.forms import ForumForm
def forum_details(request, id, template='forum/details.html'):
    d = {}
    item = get_object_or_404(Forum, pk=id)
    d['form'] = ForumForm(instance=item)
    if request.method == 'POST':
        form = ForumForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return JsonResponse(data={'form': ForumForm(instance=item).as_p(), 'token': get_token(request)})
        else:
            d['form'] = form
            return JsonResponse(data={'form': d['form'].as_p(), 'token': get_token(request)}, success=False)
    d['forum'] = Forum.objects.get(pk=id)
    return render(request, template, d)

def forum_delete(request, id):
    item = Forum.objects.get(pk=id)
    item.delete()
    return JsonResponse()

from forum.models import Topic
from forum.forms import TopicForm
def topic_list(request, template='topic/list.html'):
    d = {}
    d['form'] = TopicForm()
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            item = form.save()
            return JsonResponse(data={'id': item.id, 'name': str(item), 'form': TopicForm().as_p(), 'token': get_token(request)})
        else:
            d['form'] = form
            return JsonResponse(data={'form': d['form'].as_p(), 'token': get_token(request)}, success=False)
    d['topic_list'] = Topic.objects.all()
    return render(request, template, d)

from forum.forms import TopicForm
def topic_details(request, id, template='topic/details.html'):
    d = {}
    item = get_object_or_404(Topic, pk=id)
    d['form'] = TopicForm(instance=item)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return JsonResponse(data={'form': TopicForm(instance=item).as_p(), 'token': get_token(request)})
        else:
            d['form'] = form
            return JsonResponse(data={'form': d['form'].as_p(), 'token': get_token(request)}, success=False)
    d['topic'] = Topic.objects.get(pk=id)
    return render(request, template, d)

def topic_delete(request, id):
    item = Topic.objects.get(pk=id)
    item.delete()
    return JsonResponse()

from forum.models import Post
from forum.forms import PostForm
def post_list(request, template='post/list.html'):
    d = {}
    d['form'] = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            item = form.save()
            return JsonResponse(data={'id': item.id, 'name': str(item), 'form': PostForm().as_p(), 'token': get_token(request)})
        else:
            d['form'] = form
            return JsonResponse(data={'form': d['form'].as_p(), 'token': get_token(request)}, success=False)
    d['post_list'] = Post.objects.all()
    return render(request, template, d)

from forum.forms import PostForm
def post_details(request, id, template='post/details.html'):
    d = {}
    item = get_object_or_404(Post, pk=id)
    d['form'] = PostForm(instance=item)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return JsonResponse(data={'form': PostForm(instance=item).as_p(), 'token': get_token(request)})
        else:
            d['form'] = form
            return JsonResponse(data={'form': d['form'].as_p(), 'token': get_token(request)}, success=False)
    d['post'] = Post.objects.get(pk=id)
    return render(request, template, d)

def post_delete(request, id):
    item = Post.objects.get(pk=id)
    item.delete()
    return JsonResponse()