from django.shortcuts import render
from .models import Student, Course

# Create your views here.

def home(request):
    students=Student.objects.all()
    courses=Course.objects.all()
    context={
        'students':students,
        'courses':courses
    }
    return render(request, 'main/index.html', context)

def course_detail(request, course_id):
    courses = Course.objects.all()
    students=Student.objects.filter(course=course_id)
    context = {
        'students': students,
        'courses': courses
    }
    return render(request, 'main/course.html', context)

def student_detail(request, student_id):
    courses = Course.objects.filter(student=student_id)
    students=Student.objects.all()
    context = {
        'students': students,
        'courses': courses
    }
    return render(request, 'main/student.html', context)


