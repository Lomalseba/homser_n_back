from django.db import models

class User(models.Model):
    user_ID = models.AutoField(primary_key=True)
    login = models.TextField(unique=True)
    password = models.TextField()
    email = models.TextField(unique=True)
    full_name = models.TextField()
    role = models.TextField()

class Admin(models.Model):
    admin_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Guest(models.Model):
    guest_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class School(models.Model):
    school_ID = models.AutoField(primary_key=True)
    address = models.TextField(unique=True)
    title = models.TextField()

class Teacher(models.Model):
    teacher_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class Class(models.Model):
    class_ID = models.AutoField(primary_key=True)
    number = models.IntegerField()
    letter = models.TextField()

class Student(models.Model):
    student_ID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_ID = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)

class Subject(models.Model):
    subject_ID = models.AutoField(primary_key=True)
    title = models.TextField(unique=True)

class SubjectTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, primary_key=True)

class ClassSubject(models.Model):
    class_ID = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, primary_key=True)

class TeacherClass(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_ID = models.ForeignKey(Class, on_delete=models.CASCADE, primary_key=True)

class LabWork(models.Model):
    lab_ID = models.AutoField(primary_key=True)
    title = models.TextField(unique=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Task(models.Model):
    task_ID = models.AutoField(primary_key=True)
    lab = models.ForeignKey(LabWork, on_delete=models.CASCADE)
    number = models.IntegerField()
    description = models.TextField()

class StudentPoints(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lab = models.ForeignKey(LabWork, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class GuestPoints(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    lab = models.ForeignKey(LabWork, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
