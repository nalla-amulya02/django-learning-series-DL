from django.db import models

# Create your models here.
class Student(models.Model):
        
        name = models.CharField(max_length=100)
        age = models.IntegerField()
        email = models.EmailField()
        address = models.TextField(default="hyd")

        def __str__(self):                
              return self.name  


class Department(models.Model):
        name = models.CharField(max_length=100)

