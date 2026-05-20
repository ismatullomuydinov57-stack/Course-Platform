from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator, EmailValidator


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kurs nomi")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narx")
    description = models.TextField(verbose_name="Tavsif")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Student(models.Model):

    full_name= models.CharField(max_length=100, verbose_name="IsmFamiliya")
    phone = models.CharField(max_length=15, verbose_name="Telefon")
    address = models.TextField(blank=True, verbose_name="Manzil")
    registered_at = models.DateTimeField(auto_now_add=True)
    courses = models.ManyToManyField(Course, blank=True, verbose_name="Kurslar")

    def __str__(self):
        return f"{self.full_name}"

