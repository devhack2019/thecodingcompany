from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name="manager"),
	path('course_create/', views.courseCreate, name = 'course-create'),
	path('data/courses', views.courseList, name='course-list'),
	path('data/<str:category>', views.dataList, name='data-list'),
]
