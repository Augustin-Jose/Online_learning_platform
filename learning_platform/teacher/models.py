from django.db import models

# Create your models here.



class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(db_column='Confirm password', max_length=244)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    certificate = models.CharField(max_length=300)
    resume = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'teacher'


