from django.db import models

# Create your models here.
class CallNotice(models.Model):
    title = models.TextField()
    description = models.TextField()
    url = models.TextField(unique=True)
