from django.db import models
from get_user_data.models import students

class profile(models.Model):
    login = models.TextField()
    password = models.TextField()
    student_id = models.ForeignKey(students, on_delete=models.SET_NULL, null=True)