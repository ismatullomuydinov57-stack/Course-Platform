from django.db import models

# Create your models here.

class Course(models.Model):
    name=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    full_name=models.CharField(max_length=255)
    address=models.TextField(blank=True, null=True)
    phone_number=models.TextField()
    image=models.ImageField(upload_to='images/', blank=True, null=True)
    course=models.ManyToManyField(Course)

    def __str__(self):
        return self.full_name