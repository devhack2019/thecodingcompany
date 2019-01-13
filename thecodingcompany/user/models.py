from django.db import models
from django.contrib.auth.models import User
from attendance.models import *
# Create your models here.

######################################################################
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	rollno = models.CharField(max_length=9, blank=True)
	#############
	BRANCH_CHOICES = (
        ('CSE', 'Computer Science'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
    )
	branch = models.CharField(max_length = 3, choices = BRANCH_CHOICES, blank = True)
	##############
	teaching_assistant='TA'
	student='ST'
	professor='PR'

	EMPLOYMENT_CHOICES = (
        (teaching_assistant, 'Teaching Assistant'),
        (student, 'Student'),
        (professor, 'Professor'),
    )
	
	employment = models.CharField(max_length = 2, choices = EMPLOYMENT_CHOICES, default= student)
	###############
	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}'s Profile"