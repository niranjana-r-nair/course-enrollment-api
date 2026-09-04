from django.db import models

# Create your models here.
from django.db import models


class Course(models.Model):

    title=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    fee=models.IntegerField()
    available_seats=models.IntegerField()

    def __str__(self):
        return self.title