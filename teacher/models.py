from django.db import models

# Create your models here.

class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'teacher'

