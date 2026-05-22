from django.urls import path
from .views import home, course_detail, student_detail

urlpatterns=[
path('', home, name='home'),
    path('courses/<int:course_id>/',course_detail, name='course'),
    path('students/<int:student_id>/',student_detail, name='student')
]