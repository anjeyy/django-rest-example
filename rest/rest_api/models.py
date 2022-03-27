from django.db import models


# Create your models here.

class Document(models.Model):
    title = models.CharField(max_length=256)
    person = models.CharField(max_length=256)
    file_size = models.PositiveIntegerField()
