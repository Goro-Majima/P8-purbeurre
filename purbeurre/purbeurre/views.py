from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'grocery/home.html')

def mentions(request):
    return render(request, 'grocery/mentions.html')