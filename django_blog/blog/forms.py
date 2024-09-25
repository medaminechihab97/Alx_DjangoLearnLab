from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag
from taggit.forms import TagWidget

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PostForm(forms.ModelForm):
    # tags = forms.CharField(required=False, help_text='Enter tags separated by commas')

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }
    def clean_tags(self):
        tag_string = self.cleaned_data['tags']
        tag_names = [name.strip() for name in tag_string.split(',') if name.strip()]
        tags = []
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
        return tags
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            self.cleaned_data['tags'] = self.clean_tags()
            instance.tags.set(self.cleaned_data['tags'])
        return instance

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

