"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


from forum.models import Forum


class ForumTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')

    def tearDown(self):
        self.user.delete()

    def test_list(self):
        response = self.client.get(reverse('forum-list'))
        self.failUnlessEqual(response.status_code, 200)

    def test_crud(self):
        # Create new instance
        response = self.client.post(reverse('forum-list'), {})
        self.assertContains(response, '"success": true')

        # Read instance
        items = Forum.objects.all()
        self.failUnlessEqual(items.count(), 1)
        item = items[0]
        response = self.client.get(reverse('forum-details', kwargs={'id': item.id}))
        self.failUnlessEqual(response.status_code, 200)

        # Update instance
        response = self.client.post(reverse('forum-details', kwargs={'id': item.id}), {})
        self.assertContains(response, '"success": true')

        # Delete instance
        response = self.client.post(reverse('forum-delete', kwargs={'id': item.id}), {})
        self.assertContains(response, '"success": true')
        items = Forum.objects.all()
        self.failUnlessEqual(items.count(), 0)



from forum.models import Topic


class TopicTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')

    def tearDown(self):
        self.user.delete()

    def test_list(self):
        response = self.client.get(reverse('topic-list'))
        self.failUnlessEqual(response.status_code, 200)

    def test_crud(self):
        # Create new instance
        response = self.client.post(reverse('topic-list'), {})
        self.assertContains(response, '"success": true')

        # Read instance
        items = Topic.objects.all()
        self.failUnlessEqual(items.count(), 1)
        item = items[0]
        response = self.client.get(reverse('topic-details', kwargs={'id': item.id}))
        self.failUnlessEqual(response.status_code, 200)

        # Update instance
        response = self.client.post(reverse('topic-details', kwargs={'id': item.id}), {})
        self.assertContains(response, '"success": true')

        # Delete instance
        response = self.client.post(reverse('topic-delete', kwargs={'id': item.id}), {})
        self.assertContains(response, '"success": true')
        items = Topic.objects.all()
        self.failUnlessEqual(items.count(), 0)



from forum.models import Post


class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_user')

    def tearDown(self):
        self.user.delete()

    def test_list(self):
        response = self.client.get(reverse('post-list'))
        self.failUnlessEqual(response.status_code, 200)

    def test_crud(self):
        # Create new instance
        response = self.client.post(reverse('post-list'), {})
        self.assertContains(response, '"success": true')

        # Read instance
        items = Post.objects.all()
        self.failUnlessEqual(items.count(), 1)
        item = items[0]
        response = self.client.get(reverse('post-details', kwargs={'id': item.id}))
        self.failUnlessEqual(response.status_code, 200)

        # Update instance
        response = self.client.post(reverse('post-details', kwargs={'id': item.id}), {})
        self.assertContains(response, '"success": true')

        # Delete instance
        response = self.client.post(reverse('post-delete', kwargs={'id': item.id}), {})
        self.assertContains(response, '"success": true')
        items = Post.objects.all()
        self.failUnlessEqual(items.count(), 0)

