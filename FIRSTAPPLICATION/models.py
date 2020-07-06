from django.db import models

# Create your models here.


class Employee(models.Model):
    EmployeeID = models.CharField(max_length=50)
    EmployeeName = models.CharField(max_length=50)
    Contact = models.CharField(max_length=20)
    Address = models.CharField(max_length=200)

    class Meta:
        ordering = ['EmployeeID']

    def __str__(self):
        return self.EmployeeName
