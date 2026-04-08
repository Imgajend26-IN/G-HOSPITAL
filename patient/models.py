from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    

    def __str__(self):
        return self.name
   