from django.urls import path
from .views import dashboard_home, hospital_ai,appointment_list

urlpatterns = [
    path("", dashboard_home , name="dashboard"),
    path('ai/', hospital_ai, name='hospital_ai'),

    # path("appointments/", appointment_list, name="appointment_list")
]
