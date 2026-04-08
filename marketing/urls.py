from django.urls import path
from .views import home_page, contact_page, learn_more

urlpatterns = [
    path("",home_page, name ="home"),
    path("contact/", contact_page,name="contact"),
    path("learn_more/",learn_more, name="learn_more"),
]


