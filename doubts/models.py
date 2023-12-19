from django.db import models

# Create your models here.
class Doubts(models.Model):
    doubt_id = models.AutoField(primary_key=True)
    doubt = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    date = models.CharField(max_length=50)
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'doubts'
