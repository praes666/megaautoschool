from django.db import models

class auto(models.Model):
    brand = models.TextField()
    mark = models.TextField()
    car_number = models.CharField(max_length=10)
    photo = models.ImageField()

class workers(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    otchestvo = models.CharField(max_length=20)
    photo = models.ImageField()
    number = models.TextField(max_length=12)
    category = models.CharField(max_length=2)
    car = models.ForeignKey(auto, on_delete=models.SET_NULL, null=True)

class students(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    tel_number = models.PositiveIntegerField()
    category = models.CharField(max_length=13)
    group = models.TextField(default="Non", null=False)
    worker = models.ForeignKey(workers, on_delete=models.SET_NULL, null=True)
    drive_hours = models.PositiveIntegerField(default=60, null=False)

class lessons(models.Model):
    student = models.ForeignKey(students, on_delete=models.SET_NULL, null=True)
    worker = models.ForeignKey(workers, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    time = models.TimeField()