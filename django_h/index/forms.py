from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, ModelForm, TextInput, Textarea, ImageField, FileInput
from .models import Comments, Title, UserProfile
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


class SearchForm(Form):
    search = forms.CharField(max_length=256)


class TitleForm(ModelForm):
    class Meta:
        model = Title
        fields = ['title', 'text', 'img', 'category_name']
        widgets = {'title': TextInput(attrs={
                       'class': 'form-control',
                       'placeholder': 'Title'}),
                   'text': Textarea(attrs={
                       'class': 'form-control',
                       'placeholder': 'Text'}),
                   'img': FileInput(attrs={'class': 'form-control'})
        }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['user_name', 'user_title', 'user_comment']
        widgets = {
            'user_name': TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'User name'}),
            'user__comment': Textarea(attrs={
                     'class': 'form-control',
                     'placeholder': 'User name'}),

        }
