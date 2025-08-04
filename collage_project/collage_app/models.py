

# Create your models here.
from django.db import models

class Section(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    subject = models.CharField(max_length=100, blank=True, null=True)
    cgpa = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
