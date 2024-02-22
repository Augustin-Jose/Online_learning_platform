from django.db import models
from teacher.models import Teacher
# Create your models here.

class Tutorial(models.Model):
    class_id = models.AutoField(primary_key=True)
    video = models.URLField(max_length=25)
    notes = models.CharField(max_length=255)
    #teacher_id = models.IntegerField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tutorial'
