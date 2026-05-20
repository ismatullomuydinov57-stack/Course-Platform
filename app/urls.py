from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('courses/', course_list, name='courses'),
    path('students/', student_list, name='students'),
]