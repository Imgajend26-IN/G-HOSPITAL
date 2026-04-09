from django.urls import path
from .views import patients_edit, patient_delete, patient_create, PatientsListView, PatientListCreateAPI 
urlpatterns = [
    path("patiennts/", PatientsListView.as_view(), name="patient_list"),
    path("<int:pk>/update/", patients_edit, name="patients_edit"),
    path("<int:pk>/delete/", patient_delete, name="patient_delete"),
    path("create/", patient_create, name='patient_create'),
    path('api', PatientListCreateAPI.as_view())
    
    # path("patients/", patient_list, name='patient_list'),

    # patient_list, 

    


]
