from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patient.models import Patient
from doctors.models import Doctor

# Create your views here.
@login_required(login_url='login')
def dashboard_home(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    return render(request, "dashboard.html", {
        'patient_list': patients,
        'doctor_list': doctors
    })

@login_required
def appointment_list(request):
    return render(request, "appointment.html")