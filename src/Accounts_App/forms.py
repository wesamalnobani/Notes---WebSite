from django import forms
from .import models
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class meta:
        model = models.Profile
        fields = ['hedline', 'bio','img']

class UserForm(forms.ModelForm):
    class meta:
        model = User
        fields = ['username','first_name','last_name','email']
