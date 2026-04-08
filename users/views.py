from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout

def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]


        if User.objects.filter(username=username).exists():
         return render(request, "user_signup.html", {"error": "Username already taken"})



        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("/dashboard")
    else:
        return render(request, "user_signup.html")
    



def user_login(request):
   if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
        
# authenticate 
      user = authenticate(request, username=username , password=password)

      if user is  not None:
         login(request, user)
         return redirect("/dashboard")

      else:
         return render(request, "user_login.html", {"user":"invalid username and password"})
   else: 
      return render(request, "user_login.html")   

def user_logout(request):
    logout(request)
    return redirect("/")    
