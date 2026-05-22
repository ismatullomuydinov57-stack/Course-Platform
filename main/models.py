from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    name=models.CharField(max_length=255, verbose_name='Nomi')
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi')
    description=models.TextField(verbose_name='Tavsif')
    created_at=models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqt')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Course'
        verbose_name_plural='Courses'
        ordering=['name']



class Student(models.Model):
    full_name=models.CharField(max_length=255, verbose_name='F.I')
    address=models.TextField(blank=True, null=True, verbose_name='Manzil')
    phone_number=models.TextField(verbose_name='Tel raqam')
    image=models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Rasm')
    course=models.ManyToManyField(Course)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['full_name']




class StudentLike(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text