from django.db import models

# Create your models here.
class AA(models.Model):
    title = models.CharField(max_length=32)
    detile = models.TextField()
