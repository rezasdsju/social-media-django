from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import CustomUserCreationForm
from App_Login.models import UserProfile
from django.http import HttpResponseRedirect

from django.contrib.auth import logout
from django.shortcuts import redirect



def signup_view(request):
    form = CustomUserCreationForm()
    registerd = False
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            registerd = True
            user_profile = UserProfile(user=user)
            # login(request, user)  
            # return redirect("home")  
            return HttpResponseRedirect(reverse('App_Login:login'))
    else:
        form = CustomUserCreationForm()
        
    return render(request, "App_Login/signup.html", context={'title':'SignUp Social Media', 'form':form})


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                pass
    else:
        form = AuthenticationForm()
        
    return render(request, 'App_Login/login.html', context={'title':'login','form': form})




def logout_view(request):
    if request.method == 'POST':
        logout(request) 
        return redirect('App_Login:login')
    return redirect('App_Login:login')
   
