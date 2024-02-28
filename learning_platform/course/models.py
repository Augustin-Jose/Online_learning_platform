from django.db import models
from teacher.models import Teacher
from student.models import Student

# Create your models here.

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=255)
    description = models.CharField(db_column='Description', max_length=100)
    duration = models.CharField(max_length=255)
    course_fee = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'course'


class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    quiz = models.CharField(max_length=60)
    upload = models.CharField(max_length=400)
    date = models.TimeField()
    # teacher_id = models.IntegerField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    # student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'quiz'
