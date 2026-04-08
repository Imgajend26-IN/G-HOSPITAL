from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from appointment.models import Appointment
from patient.models import Patient
from doctors.models import Doctor

@login_required
def appointment_list(request):
    appointments = Appointment.objects.select_related('patients', 'doctors').all()
    return render(request, "appointments.html", {"appointments": appointments})

@login_required
def appointment_create(request):
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method == "POST":
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        appointment_time = request.POST.get('appointment')
        appointment_status = request.POST.get('appointment_status')

        patient = get_object_or_404(Patient, pk=patient_id)
        doctor = get_object_or_404(Doctor, pk=doctor_id)

        Appointment.objects.create(
            patients=patient,
            doctors=doctor,
            appointment=appointment_time,
            appointment_status=appointment_status,
        )
        return redirect('appointment_list')

    return render(request, "appointment_create.html", {"patients": patients, "doctors": doctors})

@login_required
def appointment_edit(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    if request.method == "POST":
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        appointment_time = request.POST.get('appointment')
        appointment_status = request.POST.get('appointment_status')

        appointment.patients = get_object_or_404(Patient, pk=patient_id)
        appointment.doctors = get_object_or_404(Doctor, pk=doctor_id)
        appointment.appointment = appointment_time
        appointment.appointment_status = appointment_status
        appointment.save()
        return redirect('appointment_list')

    return render(request, "appointment_edit.html", {
        "appointment": appointment,
        "patients": patients,
        "doctors": doctors,
    })

@login_required
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return redirect('appointment_list')
