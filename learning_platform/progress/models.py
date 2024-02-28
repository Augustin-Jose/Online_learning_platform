from django.db import models
from course.models import Course
from teacher.models import Teacher
from student.models import Student

from course.models import Quiz

# Create your models here.

class Progress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    # course_id = models.IntegerField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    progress = models.CharField(max_length=255)
    #teacher_id = models.IntegerField
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    #student_id = models.IntegerField()
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    # quiz_id = models.IntegerField()
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'progress'





