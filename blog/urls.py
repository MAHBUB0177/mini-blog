from django.contrib import admin
from django.urls import path
from.views import*

urlpatterns = [
    path('',home,name='home'),
    path('navbar/',navbar,name='navbar'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('dashboard/',dashboard,name='dashboard'),
    path('Login/',Login,name='Login'),
    path('Logout/',Logout,name='Logout'),
    path('signup/',signup,name='signup')
    
]