from django.db import models
class user(models.Model):
    Fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class referralcode(models.Model):
    code = models.CharField(max_length=20 ,unique=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)




# Create your models here.
