from django.db import models
from django.utils import timezone

# Create your models here.
class note(models.Model):
    title = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title