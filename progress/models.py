from django.db import models
<<<<<<< HEAD
from course.models import Course
from teacher.models import Teacher
from student.models import Student
=======

>>>>>>> c1edbc4fc6a75406916eeeae4b4d0b2b2164d7ce
# Create your models here.

class Progress(models.Model):
    progress_id = models.AutoField(primary_key=True)
<<<<<<< HEAD
    # course_id = models.IntegerField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    progress = models.CharField(max_length=255)
    #teacher_id = models.IntegerField
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    #student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
=======
    course_id = models.IntegerField()
    progress = models.CharField(max_length=255)
    teacher_id = models.IntegerField()
    student_id = models.IntegerField()
>>>>>>> c1edbc4fc6a75406916eeeae4b4d0b2b2164d7ce

    class Meta:
        managed = False
        db_table = 'progress'

