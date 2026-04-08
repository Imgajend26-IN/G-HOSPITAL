from django.db import models

# Create your models here.
class Appointment(models.Model): #remember one  put first app name and then model class anme
    patients = models.ForeignKey('patient.Patient', on_delete=models.CASCADE )
    doctors = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE )
    appointment = models.DateTimeField()
    appointment_status = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.patients} - {self.doctors}"
   