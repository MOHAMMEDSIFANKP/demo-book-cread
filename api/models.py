from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.PositiveIntegerField(blank=True,null=True)
    description = models.TextField(null=True,blank=True)


