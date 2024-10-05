from django.db import models

# Create your models here.
class User(models.Model):
    username = models.TextField(max_length=50)
    password = models.TextField(max_length=50)

    def __str__(self):
        return self.username

