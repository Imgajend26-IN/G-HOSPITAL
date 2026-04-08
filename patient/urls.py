from django.urls import path
from .views import patient_list, patients_edit, patient_delete, patient_create

urlpatterns = [
    path("patients/", patient_list, name='patient_list'),
    path("<int:pk>/update/", patients_edit, name="patients_edit"),
    path("<int:pk>/delete/", patient_delete, name="patient_delete"),
    path("create/", patient_create, name='patient_create'),
]
