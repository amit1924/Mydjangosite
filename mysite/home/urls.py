# APP URL


from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.homepage ,name='homepage'),
   path('index' , views.index, name='home'),
   path('about' , views.about, name='about'),
   path('services' , views.services, name='services'),
   path('contact' , views.contact, name='contact'),
]
