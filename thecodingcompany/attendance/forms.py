from django import forms
from django.contrib.auth.models import User
from .models import *

class CourseCreationForm(forms.Form):
	name = forms.CharField(max_length = 100, default = 'Course Name')
	code = forms.CharField(max_length = 5, default = 'Code')	
	