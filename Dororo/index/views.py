from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class index1(generic.TemplateView):  
    template_name="index/index.html"

class index(LoginRequiredMixin,generic.TemplateView):
    login_url="index:login"
    template_name="index/index.html"
    

