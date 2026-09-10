from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from courses.models import Course


class Enrollment(models.Model):

    student=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    enrollment_date=models.DateTimeField(auto_now_add=True)
    order_id=models.CharField(max_length=255,null=True,blank=True)
    status=models.CharField(max_length=50,default="pending")
    amount=models.IntegerField(null=True)

    def __str__(self):
        return self.student.username