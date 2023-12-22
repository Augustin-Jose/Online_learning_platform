from django.db import models
<<<<<<< HEAD
from teacher.models import Teacher
=======

>>>>>>> c1edbc4fc6a75406916eeeae4b4d0b2b2164d7ce
# Create your models here.

class Tutorial(models.Model):
    class_id = models.AutoField(primary_key=True)
    video = models.CharField(max_length=25)
    notes = models.CharField(max_length=255)
<<<<<<< HEAD
    #teacher_id = models.IntegerField()
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
=======
    teacher_id = models.IntegerField()
>>>>>>> c1edbc4fc6a75406916eeeae4b4d0b2b2164d7ce
    subject = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tutorial'
