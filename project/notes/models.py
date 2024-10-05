from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class note(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} by {self.username}"