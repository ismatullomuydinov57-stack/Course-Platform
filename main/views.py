from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Course, StudentLike

# Create your views here.

def home(request: HttpRequest):
    students = Student.objects.all()

    if request.user.is_authenticated:
        for student in students:
            if StudentLike.objects.filter(student=student,user=request.user).exists():
                student.like=True
            else:
                student.like=False
            student.save()


    courses = Course.objects.all()

    context = {
        'students': students,
        'courses': courses
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

@login_required(login_url='home')
def create_like(request, student_id):
    student=get_object_or_404(Student, pk=student_id)
    like, created =StudentLike.objects.get_or_create(student=student, user=request.user)
    if not created:
        like.delete()
    return redirect('home')
