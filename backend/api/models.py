from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.username