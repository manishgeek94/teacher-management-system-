from django.db import models


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=50)
    teacher_subjects = models.CharField(max_length=50)

    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=50)
    teacher_alloted = models.ManyToManyField(Teacher)

    def __str__(self):
        return self.student_name
