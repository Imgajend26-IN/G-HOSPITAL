from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=12)


    
    def __str__(self):
        return self.name
   