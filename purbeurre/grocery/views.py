from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'grocery/home.html')

def results(request):
    return render(request, 'grocery/results.html')

def mentions(request):
    return render(request, 'grocery/mentions.html')