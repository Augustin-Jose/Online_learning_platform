from django.db import models
from student.models import Student
from course.models import Course
# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_method = models.CharField(db_column='payment method', max_length=100)  # Field renamed to remove unsuitable characters.
    amount = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100)
    # student_id = models.IntegerField()
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    # course_id = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    class Meta:
        managed = False
        db_table = 'payment'
