
# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag
from django.forms import widgets
from taggit.forms import TagField  # Import TagField from taggit



class TagWidget(widgets.TextInput):
    def render(self, name, value, attrs=None, renderer=None):
        return super().render(name, value, attrs)


class PostForm(forms.ModelForm):
    tags = TagField()  # Use TagField for tags

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Reference to the Comment model
        fields = ['content']  # Only the content of the comment is editable by the user

    # You can add additional customization for the form fields here, such as adding custom widgets
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write your comment here...'})