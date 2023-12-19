from django.db import models

# Create your models here.

class Tutorial(models.Model):
    class_id = models.AutoField(primary_key=True)
    video = models.CharField(max_length=25)
    notes = models.CharField(max_length=255)
    teacher_id = models.IntegerField()
    subject = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tutorial'
