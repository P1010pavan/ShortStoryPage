from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from  .models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']


class upload1(forms.ModelForm):
    class Meta:
        model = upload
        fields = ['Your_Name','email','Title_of_the_story','Story_Description','Image']

class contactus(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['name','email','message']