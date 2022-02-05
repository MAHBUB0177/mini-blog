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
    path('signup/',signup,name='signup'),

    path('sales-supplier-createlist', sales_supplier_view.as_view(), name='sales-supplier-createlist'),
    path('sales-supplier-insert', sales_supplier_insert, name='sales-supplier-insert'),
    path('sales-supplier-edit/<slug:id>', sales_supplier_edit, name='sales-supplier-edit'),
    
]