from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render( request,"doc_list.html" ,{"doctors":doctors})

@login_required
def doctors_edit(request, pk):
    
    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == "POST":
        doctor.name = request.POST.get('name')
        doctor.specialization = request.POST.get('specialization')
        doctor.phone = request.POST.get('phone')
        doctor.save()
        return redirect("doctor_list") #ye url ko redirect karta hai
    return render (request,"doctors_edit.html", {"doctor":doctor})

@login_required
def doctors_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    doctor.delete()
    return redirect("doctor_list")

@login_required
def doctors_create(request):
    if request.method == "POST":
       name =  request.POST.get('name')
       specialization = request.POST.get('specialization')
       phone = request.POST.get('phone')
       email = request.POST.get('email')

       Doctor.objects.create(
           name=name,
           specialization=specialization,
           phone=phone,
           email=email
       )
       return redirect('doctor_list')
    return render(request,"doctors_create.html")



from rest_framework.generics import ListCreateAPIView
from .serializers import DoctorSerializer

class DoctorListCreateApiView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer