from django.shortcuts import render, HttpResponse
# from datetime import datetime
from home.models import Contact
import requests
import json
from django.contrib import messages

# Create your views here.


def homepage(request):
    context = {
        'variable1': 'this is a sample1',
        'variable2': 'this is a sample2',
    }
    # messages.success(request, "your form submitted.")
    return render(request, 'index.html', context)


def index(request):
    #  return HttpResponse('this is home page')
    return render(request, '.html')


def about(request):
    #  return HttpResponse('this is about page')
    return render(request, 'about.html')


def services(request):
    #  return HttpResponse('this is services page')
    return render(request, 'services.html')


def contact(request):
    #  return HttpResponse('this is contact page')
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        contact = Contact(name=name, mobile=mobile)
        contact.save()
        messages.success(request, "your form submitted.")
    return render(request, 'contact.html')
