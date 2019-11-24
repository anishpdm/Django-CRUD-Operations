from django.db import models

# Create your models here.

class Books(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=10)
    description=models.TextField()
    genre=models.CharField(max_length=50)
