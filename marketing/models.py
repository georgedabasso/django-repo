from django.db import models
class user(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class referralcode(models.Model):
    code = models.CharField(max_length=20 ,unique=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)

class products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(null=False)




# Create your models here.
