from django.urls import path
from .views import doctors_list, doctors_edit, doctors_delete, doctors_create,DoctorListCreateApiView

urlpatterns = [
     path("doctor/", doctors_list, name='doctor_list'), # redirect name ye hota hai
     path("<int:pk>/update/",doctors_edit,name="doctors_edit"), #this name jab hum render karne time hote hai
     path("<int:pk>/delete/", doctors_delete, name="doctors_delete"),
     path("create/", doctors_create,name='doctors_create'),
      path('api', DoctorListCreateApiView.as_view())

]

