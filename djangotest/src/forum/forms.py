from django import forms


from forum.models import Forum

class ForumForm(forms.ModelForm):
    """Form assistant class"""
    class Meta:
        model = Forum


from forum.models import Topic
class TopicForm(forms.ModelForm):
    """Form assistant class"""
    class Meta:
        model = Topic
        fields = ('title',)


from forum.models import Post
class PostForm(forms.ModelForm):
    """Form assistant class"""
    class Meta:
        model = Post
        fields = ('title', 'body')
