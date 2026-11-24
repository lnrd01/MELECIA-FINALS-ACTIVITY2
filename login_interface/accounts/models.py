from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.username