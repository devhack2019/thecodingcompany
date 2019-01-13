from django.contrib.auth.models import User
from django.db.models import Q
import re
from django.core.mail import send_mail
from NowWeSeeYou.settings import EMAIL_HOST_USER 
from .models import *

def notify(filename, course):
	#reads a file that has row as filename
	file = open(filename, 'r')
	present_email = []
	course.classes_held += 1
	course.save()
	for email in file:
		present_email.append(email.rstrip())
	#users 
	all_students = course.people.all().filter(profile__employment = 'ST')
	absentees = []
	for student in all_students:
		#take attendance
		if student.email in present_email:
			a1 = Attendance(course = course, student = student, isPresent = True)
		else:
			a1 = Attendance(course = course, student = student, isPresent = False)
			absentees.append(student.email)
		a1.save()
	send_mail(f'Absent for {course}',
			'You were absent for this class',
			EMAIL_HOST_USER,
			absentees)

def prepareData(tas, students, profs):
	tas = list(map(int,tas))
	profs = list(map(int,profs))
	stud_list = re.sub('[\s+]', '', students).split(',')
	students = []
	for thing in stud_list:
		if '-' in thing:
			students+=makeRange(thing)
		else:
			students.append(thing)
	print(students)
	people = User.objects.filter(Q(id__in = tas+profs) | Q(profile__rollno__in = students))
	return people

def makeRange(s):
	start, finish = s.split('-')
	s =  list(range(int(start), int(finish)+1))
	s = list(map(str, s))
	return s