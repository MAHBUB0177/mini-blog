from django.shortcuts import render


from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from.forms import User,SignUpForm
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse


def home(request):
  return render(request,'blog/home.html')

def navbar(request):
  return render(request,'blog/navbar.html')

def about(request):
  return render(request,'blog/about.html')

def contact(request):
  return render(request,'blog/contact.html')

def dashboard(request):
  return render(request,'blog/dashboard.html')

def Login(request):
  return render(request,'blog/Login.html')

def Logout(request):
  return render(request,'blog/Log out.html')

def signup(request):
  data=dict()
  form=SignUpForm()
  # data['form']=form
  return render(request,'blog/sign-up.html',{'form':form})