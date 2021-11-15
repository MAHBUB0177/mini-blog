from typing import AbstractSet
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets

# from.models import*

class SignUpForm(UserCreationForm):

  password1=forms.CharField(label=' Password',widget=forms.PasswordInput())
  def __init__(self, *args, **kwargs):
      super(SignUpForm, self).__init__(*args, **kwargs)
  class Meta:
        model =User
        fields = ("username",'first_name','last_name','email')
        labels={
          'first_name':('First_name'),
          'last_name':('Last Name'),
          'email':('Email'),

        }
        widgets={
          'username':forms.TextInput(attrs={'class':'form-control'}),
          'forst_name':forms.TextInput(attrs={'class':'form-control'}),
          # 'forst_name':forms.TextInput(attrs={'class':'form-control'}),
          'last_name':forms.TextInput(attrs={'class':'form-control'}),
          'email':forms.TextInput(attrs={'class':'form-control'}),
        }

    
