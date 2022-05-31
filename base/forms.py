
from django.forms import ModelForm
from .models import *
from django import forms

class UserForm(ModelForm):

    class Meta:
        model = User
        fields =  ['mobile', 'password']