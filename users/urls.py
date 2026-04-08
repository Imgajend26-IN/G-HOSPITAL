from django.urls import path
from .views import sign_up, user_login, user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("login/",user_login, name= "login"),
    path("logout/", user_logout, name="logout"),
]