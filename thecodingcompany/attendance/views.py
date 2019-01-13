from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import re
from django.db.models import Q
from django.contrib import messages
from .models import *
from .helpers import *
# Create your views here.
def home(request):
	context = {}
	if request.user.is_authenticated:
		temp = request.user.course_set.all()	
		context['courses'] = []
		if request.method == 'POST':
			course = Course.objects.get(name = 'Calculus')
			notify('real_time_count.txt', course)
		for course in temp:
			#get attendance of request.user
			n = request.user.attendance_set.all().filter(course = course, isPresent=True).count()
			frac = 100*n/course.classes_held
			color = 'success'
			if frac > 80 and frac<85:
				color = 'warning'
			elif frac < 80:
				color = 'danger'
			context['courses'].append((course, round(frac), n, color))
	return render(request, 'attendance/manager.html', context)

def courseCreate(request):
	context = {}
	people = User.objects.all()
	context['tas'] = people.filter(profile__employment = 'TA').order_by('first_name', 'last_name')
	context['profs'] = people.filter(profile__employment = 'PR').order_by('first_name', 'last_name')

	if request.method == 'POST':
		if 'tas' not in request.POST:
			messages.info(request, 'Select atleast one teaching assistant')
		elif 'profs' not in request.POST:
			messages.info(request, 'Select atleast one professor')
		else:
			ppl = prepareData(request.POST.getlist('tas'), request.POST['students'], request.POST.getlist('profs'))
			course = Course(name = request.POST['name'], code = request.POST['code'])
			course.save()
			for person in ppl:
				course.people.add(person)
			messages.success(request, f'{course} created successfully')
	return render(request, 'attendance/course_create.html', context)


def courseList(request):
	if request.method == 'POST':
		if 'todelete' in request.POST:
			courses = list(map(int, request.POST.getlist('todelete')))
			Course.objects.filter(pk__in = courses).delete()
			messages.success(request, 'Courses deleted successfully')
	context = {
		'courses': Course.objects.all()
	}
	context['heading'] = "Courses"
	return render(request, 'attendance/course_list.html', context)

def dataList(request, category):
	context = {}
	if request.method == 'POST':
		if 'todelete' in request.POST:
			users = list(map(int, request.POST.getlist('todelete')))
			User.objects.filter(pk__in = users).delete()
			messages.success(request, 'Accounts deleted successfully')
	people = User.objects.all()
	context['people'] = people.filter(profile__employment = category.upper()).order_by('first_name', 'last_name')
	context['heading'] = context['people'].first().profile.get_employment_display()+'s'
	return render(request, 'attendance/data_list.html', context)
