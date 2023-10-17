import datetime

from django.db import models
from django.utils import timezone

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
    pub_date = models.DateTimeField("date published", default=timezone.now(), null=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def was_published_recently(self):
        return self.pub_date >= timezone(now) - datetime.timedelta(days=1)



