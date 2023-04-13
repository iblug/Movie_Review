from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    movie = models.CharField(max_length=20)