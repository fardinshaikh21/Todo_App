from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(request, "{% url 'register' %}", {"error": "Passwords do not match."})

        if username and password:

            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect("login")
        
    return render(request, "{% url 'register' %}")    

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "{% url 'login' %}", {"error": "Invalid username or password."})

    return render(request, "{% url 'login' %}")

def logout_view(request):
    logout(request)
    return redirect("login")
