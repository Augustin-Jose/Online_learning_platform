from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    payment_method = models.CharField(db_column='payment method', max_length=100)  # Field renamed to remove unsuitable characters.
    amount = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100)
    username = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'payment'
