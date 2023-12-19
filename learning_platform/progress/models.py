from django.db import models

# Create your models here.

class Progress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    progress = models.CharField(max_length=255)
    teacher_id = models.IntegerField()
    student_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'progress'

