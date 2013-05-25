from django import forms


from forum.models import Forum

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum


from forum.models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic


from forum.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
