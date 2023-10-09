from django.db import models

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} {self.last_name}"



