from django.db import models

# Create your models here.
class Department(models.Model):
    deptName = models.CharField(max_length = 100, unique=True)

    def __str__(self):
        return self.deptName

class Employee(models.Model):
    empfName = models.CharField(max_length = 100)
    emplName = models.CharField(max_length = 100)
    phone = models.CharField(max_length= 15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __Str__(self):
        return self.empfName

