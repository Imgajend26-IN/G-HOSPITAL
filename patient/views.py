from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from django.contrib.auth.decorators import login_required
from django import views
from django .utils.decorators import method_decorator
from urllib import request
# @login_required
# def patient_list(request):
#     patients = Patient.objects.all()
#     return render(request,"list.html" ,{"patients":patients} )

class PatientsListView(views.View):
        
        def get(self, request):
             patients = Patient.objects.all()
             return render(request,"list.html",{"patients":patients})
        

@login_required
def patients_edit(request, pk):

    patient = get_object_or_404(Patient, pk=pk)

    if request.method == "POST":

        patient.name = request.POST.get('name')
        patient.phone = request.POST.get('phone')
        patient.email = request.POST.get('email')
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
        email = request.POST.get('email')

        Patient.objects.create(
            name=name,
            phone=phone,
            email=email
        )
        return redirect('patient_list')
    return render(request,"patient_create.html")

from rest_framework.generics import ListCreateAPIView
from .serializers import PatientSerializer

class PatientListCreateAPI(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer