from django.db import models

# Create your models here.

class departments(models.Model):
    dept_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class employe(models.Model):
    emp_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    dept=models.ForeignKey(departments,on_delete=models.CASCADE)

    def __str__(self):
        return self.name