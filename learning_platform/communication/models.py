from django.db import models

# Create your models here.
class Communication(models.Model):
    comm_id = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=100)
    date = models.CharField(max_length=15)
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'communication'

