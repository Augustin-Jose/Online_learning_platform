from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    course_fee = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'course'
