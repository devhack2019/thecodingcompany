from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from user.models import *

# Create your models here.
class Course(models.Model):
	people = models.ManyToManyField(User, blank = True)
	code = models.CharField(max_length=6, default='code')
	name = models.CharField(max_length=100, default='Course Name')
	next_class = models.DateTimeField(blank=True, default = timezone.now)
	being_held = models.BooleanField(default = False)
	classes_held = models.IntegerField(default = 0)
	
	def __str__(self):
		return f'{self.code} {self.name}'

	class Meta:
		ordering = ['name']


class Attendance(models.Model):
	course = models.ForeignKey(Course, on_delete = models.CASCADE)
	student = models.ForeignKey(User, on_delete = models.CASCADE)
	isPresent = models.BooleanField(default = False)
	day = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return f'{self.student.rollno} {self.course.code} {self.isPresent}'	
		