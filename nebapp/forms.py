from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Neighbourhood,Post,Business,Location,Comment,Profile
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        
        exclude =['user']

class NewHoodForm(forms.ModelForm):
    class Meta:
        model= Neighbourhood
        # fields = ['name','description','location','police_contact','hospital_contact']
        exclude =['user','admin']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model= Business
        exclude=['user','hood','admin']

class NewPostForm(forms.ModelForm):
    class Meta:
        model= Post
        exclude=['user','hood']


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user','post']