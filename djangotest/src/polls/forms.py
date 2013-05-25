
from django import forms
from models import *



class UserForm(forms.ModelForm):
	
    class Meta:
        model = User	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

