from django.db import models

# Create your models here.
#
# class Student(models.Model):
#     student_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     gender = models.CharField(max_length=50)
#     age = models.CharField(max_length=50)
#     status = models.CharField(max_length=50)
#     address = models.CharField(max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'student'

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(db_column='Confirm password', max_length=244)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'student'

