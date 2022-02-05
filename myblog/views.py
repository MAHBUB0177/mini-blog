from website.models import *
from django.shortcuts import render
# from websites.models import Website

def home_view(request):
    name = "Welcome to"

    obj = Website.objects.get(id=2)

    context = {
        'name': name,
        'obj' : obj,
    }

    return render(request, 'home.html', context)


def barcode_view(request):
    name="welcome to"
    obj=Product.objects.get(id=1)

    context={
        'name':name,
        'obj':obj
    }

    return render(request,"barcode_html",context)