
from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.signup_view, name='sign_up'), 
    path('login/',views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
]
