from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from django.contrib.auth.decorators import login_required

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request,"list.html" ,{"patients":patients} )

@login_required
def patients_edit(request, pk):

    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":

        patient.name = request.POST.get('name')
        patient.phone = request.POST.get('phone')
        patient.save()
        return redirect("patient_list")
    return render(request,"patients_edit.html",{"patient":patient})


@login_required
def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect("patient_list")

@login_required
def patient_create(request):
    if request.method =="POST":
        name = request.POST.get('name'),
        phone = request.POST.get('phone')

        Patient.objects.create(
            name=name,
            phone=phone
        )
        return redirect('patient_list')
    return render(request,"patient_create.html")