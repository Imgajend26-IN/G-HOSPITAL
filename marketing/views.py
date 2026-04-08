from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "marketing.html")


def contact_page(request):
    return render(request,"contact.html")

def learn_more(request):
  return render(request,"learn_more.html")    



# def signup(request):
#     return render(request, "signup.html")


# def login_view(request):
#     return render(request, "login.html")


# def contact(request):
#     return render(request, "contact.html")