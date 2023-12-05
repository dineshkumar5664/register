from django.db import models


# Create your models here.
class Employees(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=15)
    empphno = models.IntegerField()
    empsalary = models.IntegerField()
    empaddress = models.CharField(max_length=20)

    def __str__(self):
        return self.empname
