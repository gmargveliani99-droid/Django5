from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price=models.FloatField()

    def __str__(self):
        return self.name
    
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Course(models.Model):
    title=models.CharField(max_length=100)
    duration=models.IntegerField()
    def __str__(self):
        return self.title
    
        
           
