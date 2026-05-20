from django.shortcuts import render
from .models import Course, Student


def home(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, 'app/index.html', context)


def about(request):
    return render(request, 'app/about.html')


def course_list(request):
    courses = Course.objects.all()

    context = {
        'courses': courses
    }

    return render(request, 'app/courses.html', context)


def student_list(request):
    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'app/students.html', context)