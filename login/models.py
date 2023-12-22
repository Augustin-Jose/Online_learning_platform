from django.db import models

<<<<<<< HEAD

=======
>>>>>>> c1edbc4fc6a75406916eeeae4b4d0b2b2164d7ce
# Create your models here.

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'
