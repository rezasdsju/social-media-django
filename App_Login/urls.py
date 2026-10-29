# your_app_name/urls.py
from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup_view, name='sign_up'), 
]
