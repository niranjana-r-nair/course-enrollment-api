from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from courses.models import Course


class Enrollment(models.Model):

    student=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    enrollment_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username