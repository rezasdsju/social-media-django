from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm



def signup_view(request):
    form = CustomUserCreationForm()
    registerd = False
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            registerd = True
            login(request, user)  
            # return redirect("home")  
    else:
        form = CustomUserCreationForm()
        
    return render(request, "App_Login/signup.html", context={'title':'SignUp Social Media', 'form':form})