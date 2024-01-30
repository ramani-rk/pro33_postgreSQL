from django.db import models

# Create your models here.

class Dept(models.Model):
    Dno=models.IntegerField()
    Dname=models.CharField(max_length=100)
    Dloc=models.CharField(max_length=100)

    def __str__(self):
        return self.Dname