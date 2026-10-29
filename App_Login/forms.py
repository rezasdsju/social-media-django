from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
  username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'myusername'}))
  email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'abc@email.com'}))
  first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder':'Jolil'}))
  last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(attrs={'placeholder':'Khan'}))

  class Meta:
    model = User
    fields = ("username", "email", "first_name", "last_name", "password1", "password2")