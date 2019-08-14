from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'grocery/home.html')

def list(request):
    return render(request, 'grocery/list.html')