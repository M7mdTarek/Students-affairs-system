from pyexpat import model
from tabnanny import verbose
from unicodedata import decimal
from django.db import models

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=15)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    Id = models.IntegerField(primary_key=True)
    date = models.DateField()
    gender = models.CharField(max_length=5 , null=True )
    level = models.CharField(max_length=10 , null=True )
    status = models.BooleanField(default=True , null=True )
    dep = models.CharField(max_length=10,null=True)
    email = models.CharField(max_length=10)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        #verbose_name = 'student'
        ordering = ['-gpa']