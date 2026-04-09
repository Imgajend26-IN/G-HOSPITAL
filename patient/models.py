from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, null=True, blank=True)

    

    def __str__(self):
        return self.name
   