from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


#create your forms here
class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class ProfileCreationForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['rollno', 'branch', 'employment']