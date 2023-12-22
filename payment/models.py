from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    payment_method = models.CharField(db_column='payment method', max_length=100)  # Field renamed to remove unsuitable characters.
    amount = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'payment'
