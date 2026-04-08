from django.urls import path
from .views import dashboard_home, appointment_list

urlpatterns = [
    path("", dashboard_home , name="dashboard"),
    # path("appointments/", appointment_list, name="appointment_list")
]
