from django import forms
from django.forms import ModelForm
from .models import Post, Commentary, Profile


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'post_image')
        labels = {
            'title': '',
            'text': '',
            'post_image': '',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'})
        }


class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('name', 'bio', 'email', 'profile_pic')
        labels = {
            'name': '',
            'bio': '',
            'email': '',
            'profile_pic': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }